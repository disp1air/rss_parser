import unittest
from rssparser.get_args import get_args


class TestGetArgs(unittest.TestCase):
    def test_get_args(self):
        args = get_args()
        self.assertEqual(args.limit, None)


if __name__ == '__main__':
    unittest.main()
