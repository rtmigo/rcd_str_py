import unittest

from rcd_str import minimize_spaces, remove_empty_lines


class TestMinimizeSpaces(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(
            minimize_spaces('  some   words with\n\t  spaces   '),
            'some words with spaces')

    def test_keep_new(self):
        self.assertEqual(
            minimize_spaces('  first  \n  second line  \n\n and the last one ',
                            keep_newlines=True),
            'first\nsecond line\n\nand the last one')


class TestRemoveEmptyLines(unittest.TestCase):
    def test_before(self):
        self.assertEqual(
            remove_empty_lines('\none\ntwo\nthree'),
            'one\ntwo\nthree')
        self.assertEqual(
            remove_empty_lines('\n\none\ntwo\nthree'),
            'one\ntwo\nthree')

    def test_after(self):
        self.assertEqual(
            remove_empty_lines('one\ntwo\nthree\n'),
            'one\ntwo\nthree')
        self.assertEqual(
            remove_empty_lines('one\ntwo\nthree\n\n'),
            'one\ntwo\nthree')

    def test_simple(self):
        self.assertEqual(
            remove_empty_lines('one\ntwo\nthree'),
            'one\ntwo\nthree')
        self.assertEqual(
            remove_empty_lines('one\n\n\n\ntwo\n\n\nthree'),
            'one\ntwo\nthree')

        # а тут пробел:
        self.assertEqual(
            remove_empty_lines('one\n\n \n\ntwo\n\n\nthree'),
            'one\n \ntwo\nthree')
