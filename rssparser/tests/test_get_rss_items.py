from rssparser.get_rss_items import get_rss_items
import unittest
from xml.etree.ElementTree import Element


class TestRssParser(unittest.TestCase):
    def test_get_rss_items(self):
        item_element = Element('item')
        not_item_element = Element('title')

        self.assertEqual(get_rss_items([[]]), [])
        self.assertEqual(
            get_rss_items([[item_element]]),
            [item_element]
        )
        self.assertEqual(
            get_rss_items([[item_element, not_item_element, item_element]]),
            [item_element, item_element]
        )


if __name__ == '__main__':
    unittest.main()
