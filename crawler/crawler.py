# ugh, monkey patch required because python != nice concurrency
from gevent import monkey
monkey.patch_all()

from urllib.parse import urlparse, urljoin
import urllib.robotparser

from gevent.queue import Queue, Empty
from bs4 import BeautifulSoup
import multiprocessing
import httplib2
import gevent


# HTTP heads sent with request
HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# Crawler level depth
# 1 would just download the target, 2 downloads target and immediate links, 3 is links of immediate links
MAX_LEVEL = 1

# Crawl Delay (in seconds)
# This should be a standards compliant crawler not a DDoS machine
# PS: use the value given by robots.txt in production
CRAWL_DELAY = 1



# Links scheduled by controller
# Consumer: speedo_worker; Publisher: speedo_controller
download_queue = Queue(maxsize=multiprocessing.cpu_count())  # Queue<SpeedoJob>

# Links pending review by controller
# Consumer: speedo_controller; Publisher: speedo_worker
review_queue = Queue(maxsize=8)  # Queue<SpeedoResult>


class SpeedoJob:
    """
    Holds a single async job in download_queue
    """
    def __init__(self, url, level):
        self.url = url
        self.level = level
        
class SpeedoResult:
    """
    Single Crawl session result
    Contails the target, extracted URLs and entire HTML raw body
    """
    def __init__(self, url, links, body, level):
        self.body = body
        self.url = url
        self.links = links
        self.level = level

class SpeedoCrawlReport:
    """
    Complete report for a crawling Session
    Includes responses, summaries and counters
    """
    def __init__(self):
        self.discovered = set()
        self.crawled = set()
        self.responses = []

class SpeedoSession:
    """
    Crawing Session
    Contains target domains, parsed targed and robots.txt
    """
    def __init__(self, target):
        cmp = urlparse(target)

        if cmp.scheme is None or len(cmp.scheme) == 0:
            raise SpeedoError("Provided target does not include scheme. Did you add http:// ?")

        self.domain = target
        self.base_domain = cmp.netloc

        print("[+] Fetching robots.txt")
        self.robots = urllib.robotparser.RobotFileParser()
        self.robots.set_url(urljoin(self.domain, "/robots.txt"))
        self.robots.read()

        print("[I] robots.txt processed")

def speedo_worker(w_num, session):
    """
    Async Worker
    Responsible for downloading a single URL, parsing HTML and extracting links
    """
    try:
        while True:
            job = download_queue.get(timeout=5)
            print(f'[I] Worker:{w_num} processing L{job.level} {job.url}')

            h = httplib2.Http("/tmp/speedo-cache")
            resp_header, resp_content = h.request(job.url, method="GET", headers=HEADERS)

            if resp_header['status'] != '200':
                print("[E] Status %s while downloading %s" % (resp_header['status'], job.url))
                continue

            # we can add here some smart retrying
            # sites often block with 403 when there's too many requests coming trough
            # to avoid that, we can do exponential backoff, sleeping workers and then retrying the URL
            # for now, we'll take the hit and just dismiss a 403 response

            soup = BeautifulSoup(resp_content, 'html.parser')

            a_tags = soup.find_all("a")
            links = set()

            for link in a_tags:
                href = link.get('href')

                # non href links used mostly by JS triggers, we can safely ignore them
                if href is None or len(href) == 0:
                    continue

                # local links are not relevant for our crawler
                if href.startswith("#"):
                    continue

                # relative links missing the domain, let's add it in
                if not href.startswith("http://") and not href.startswith("https://"):
                    href = urljoin(session.domain, href)

                # retrict to links only on the same base domain
                if urlparse(href).netloc != session.base_domain:
                    continue

                links.add(href)

            review_queue.put(SpeedoResult(
                url=job.url, links=list(links), body=resp_content, level=(job.level + 1)
            ))

            gevent.sleep(CRAWL_DELAY)
    except Empty:
        print(f'[I] Worker #{w_num} Tasks completed')
        
def speedo_controller(session):
    """
    Master Controller
    Triggers the initial homepage download and schedules the links discovered while crawling
    """
    scr = SpeedoCrawlReport()

    scr.crawled.add(session.domain)
    download_queue.put(SpeedoJob(session.domain, 1))

    try:
        while True:
            job_result = review_queue.get(timeout=5)
            scr.responses.append(job_result)

            for link in job_result.links:
                # respect robots.txt access restrictions
                if not session.robots.can_fetch("*", link):
                    continue

                # avoid re-crawling URLs
                if link in scr.crawled:
                    continue
                
                # download the next level
                # only allow a maximum depth for crawling
                if job_result.level <= MAX_LEVEL:
                    download_queue.put(SpeedoJob(link, job_result.level))
                    scr.crawled.add(link)

                scr.discovered.add(link)

    except Empty:
        print('[I] Controller Tasks completed')
    
    return scr

class SpeedoError(Exception):
    pass

class Speedo:
    """
    Base application class
    """
    def __init__(self, target):
        self.session = SpeedoSession(target)
        self.scr = None

    def crawl(self):
        """
        Triggers a crawling session
        """
        controller = gevent.spawn(speedo_controller, self.session)

        gevent.joinall([
            controller,

            # workers
            gevent.spawn(speedo_worker, 1, self.session),
            gevent.spawn(speedo_worker, 2, self.session),
            gevent.spawn(speedo_worker, 3, self.session),
        ])

        self.scr = controller.value

    def report(self):
        """
        Prints links hierarchy report
        """
        print("\n")
        print("[SUMMARY]")
        print("Crawled:     %d pages" % len(self.scr.crawled))
        print("Discovered:  %d links" % len(self.scr.discovered))
        print("Responses:   %d requests" % len(self.scr.responses))
        print("Errors:      %d requests" % (len(self.scr.crawled) - len(self.scr.responses)))

        print("\n")
        print("[HIERARCHY]")

        for report in self.scr.responses:
            print(f"| {report.url}")
            
            for link in report.links:
                print("| %s> %s" % (
                    "".join(["-" for y in range(0, report.level)]),
                    link
                ))


