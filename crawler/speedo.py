from crawler import Speedo


import argparse

parser = argparse.ArgumentParser(description='Crawls target domain using ')
parser.add_argument('domain', help="Starting domain name")
args = parser.parse_args()

if __name__ == "__main__":
    spider = Speedo(args.domain)
    spider.crawl()
    spider.report()
