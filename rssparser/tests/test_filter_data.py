from rssparser.filter_data import filter_by_date, filter_by_limit
import unittest


class TestFilterData(unittest.TestCase):
    def test_filter_by_date(self):
        self.assertEqual(filter_by_date(
            [{'pubDate': '2021-06-24T16:23:45Z'},
            {'pubDate': '2021-06-23T16:23:45Z'}],
            '20210623'),
            [{'pubDate': '2021-06-23T16:23:45Z'}])

    def test_filter_by_limit(self):
        self.assertEqual(filter_by_limit(
            [{'pubDate': '2021-06-24T16:23:45Z'},
            {'pubDate': '2021-06-23T16:23:45Z'},
            {'pubDate': '2021-07-21T11:22:44Z'}],
            1),
            [{'pubDate': '2021-06-24T16:23:45Z'}])

if __name__ == '__main__':
    unittest.main()
