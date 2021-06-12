import io
import unittest
from unittest import mock
from xml.etree.ElementTree import Element
from print_rss_item import print_rss_item, print_child_exept_items


class TestPrintRssItem(unittest.TestCase):
    def test_print_rss_item(self):
        item_element = Element('item')
        self.assertEqual(print_rss_item([item_element]), None)

        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print_rss_item([item_element])

        self.assertEqual(
            fake_stdout.getvalue(),
            'item\n=============================================\n'
        )

        item_element.text = 'test1'
        self.assertEqual(print_rss_item([item_element]), None)

    def test_print_child_exept_items(self):
        item_element = Element('item')
        self.assertEqual(print_child_exept_items([item_element]), None)

        item_element.text = 'test1'
        self.assertEqual(print_child_exept_items([item_element]), None)


if __name__ == '__main__':
    unittest.main()
