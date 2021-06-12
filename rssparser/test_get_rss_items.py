from get_rss_items import get_rss_items, get_child_exept_items
import unittest
from xml.etree.ElementTree import Element


class TestRssParser(unittest.TestCase):
    def test_get_rss_items(self):
        item_element = Element('item')
        not_item_element = Element('title')
        # if there is no limit
        self.assertEqual(get_rss_items([[]], None), [])
        self.assertEqual(
            get_rss_items([[item_element, not_item_element]], None),
            [item_element]
        )
        # if there is limit
        self.assertEqual(get_rss_items([[]], 1), [])
        self.assertEqual(
            get_rss_items([[item_element, not_item_element, item_element]], 1),
            [item_element]
        )

    def test_get_child_exept_items(self):
        item_element = Element('item')
        not_item_element = Element('title')
        self.assertEqual(get_child_exept_items([[]]), [])
        self.assertEqual(get_child_exept_items([[item_element]]), [])
        self.assertEqual(
            get_child_exept_items([[not_item_element]]),
            [not_item_element]
        )


if __name__ == '__main__':
    unittest.main()
