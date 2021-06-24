import io
import unittest
from unittest import mock
from rssparser.verbose_module import print_verbose


class TestVerbodeModule(unittest.TestCase):
    def test_print_verbose(self):
        self.assertEqual(print_verbose([{}]), None)

        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print_verbose([{'title': 'test_title'}])

        self.assertEqual(
            fake_stdout.getvalue(),
            'title: test_title\n===================================\n'
        )


if __name__ == '__main__':
    unittest.main()
