from pathlib import Path
import unittest

from mocket import mocketize
from mocket.mockhttp import Entry

from crawler import Speedo


class SpeedoTestCases(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mocketize
    def test_hacker_news(self):
        Entry.single_register(
            Entry.GET,
            "http://news.ycombinator.com",
            body=Path('fixtures/homepage.html').read_text(),
            headers={'content-type': 'text/html; charset=UTF-8'}
        )

        Entry.single_register(
            Entry.GET,
            "http://news.ycombinator.com/robots.txt",
            body=Path('fixtures/robots.txt').read_text(),
            headers={'content-type': 'text/plain'}
        )

        spider = Speedo("http://news.ycombinator.com")
        spider.crawl()

        spider.report()

        self.assertEqual(len(spider.scr.crawled), 1)
        self.assertEqual(len(spider.scr.discovered), 128)
        self.assertEqual(len(spider.scr.responses), 1)
