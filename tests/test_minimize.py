import unittest

from rcd_str import minimize_spaces


class TestMinimize(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            minimize_spaces('  some   words with\n\t  spaces   '),
            'some words with spaces')

    def test_keep_new(self):
        self.assertEqual(
            minimize_spaces('  first  \n  second line  \n\n and the last one ',
                            keep_newlines=True),
            'first\nsecond line\n\nand the last one')

