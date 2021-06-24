import unittest
from unittest.mock import create_autospec
from rssparser.convert_module import rss_items_to_list, rss_to_dict


class TestConvertModule(unittest.TestCase):
    def test_rss_items_to_list(self):
        self.assertEqual(rss_items_to_list([{}]), [{}])


    def test_rss_to_dict(self):
        self.assertEqual(rss_to_dict([{}]), {'item1': {}})

if __name__ == '__main__':
    unittest.main()
