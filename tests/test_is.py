import unittest

from rcd_str import is_blank


class TestIs(unittest.TestCase):
    def test_is_blank(self):
        self.assertFalse(is_blank('hi'))
        self.assertFalse(is_blank(' hi '))
        self.assertFalse(is_blank('hi\n'))
        self.assertFalse(is_blank('\nhi\n'))
        self.assertTrue(is_blank(' '))
        self.assertTrue(is_blank('\n'))
        self.assertTrue(is_blank(' \n '))
        self.assertTrue(is_blank(' \n\r\n \n \r \t '))
