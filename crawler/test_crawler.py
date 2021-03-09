from unittest.mock import patch
from pathlib import Path
import unittest

from mocket import mocketize
from mocket.mockhttp import Entry

from crawler import Speedo

def mocked_requests_get(*args, **kwargs):
    return {'status': '200'}, Path('fixtures/homepage.html').read_text()

class SpeedoTestCases(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mocketize
    @unittest.mock.patch('crawler.MAX_LEVEL', 1)
    def test_hacker_news(self):
        Entry.single_register(
            Entry.GET,
            "http://news.ycombinator.com/robots.txt",
            body=Path('fixtures/robots.txt').read_text(),
            headers={'content-type': 'text/plain'}
        )

        with patch('crawler.download_url', side_effect=mocked_requests_get):
            spider = Speedo("http://news.ycombinator.com")
            spider.crawl()

        spider.report()

        self.assertEqual(len(spider.scr.crawled), 1)
        self.assertEqual(len(spider.scr.discovered), 129)
        self.assertEqual(len(spider.scr.responses), 1)
