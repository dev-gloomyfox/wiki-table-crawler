import unittest

from wiki_table_crawler.crawl import crawl


class CrawlTestCase(unittest.TestCase):
    def test_crawl(self):
        self.assertEqual(2, crawl(1), msg="Expect message")


if __name__ == "__main__":
    unittest.main()
