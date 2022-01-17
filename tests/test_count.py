import unittest

from rcd_str import count_letters, count_cyrillic, count_digits


class TestCount(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(count_letters(''), 0)
        self.assertEqual(count_letters(' \n '), 0)
        self.assertEqual(count_letters('abc'), 3)
        self.assertEqual(count_letters('  abc de '), 5)
        self.assertEqual(count_letters(' абыр валг '), 8)
        self.assertEqual(count_letters(' абыр_валг 782 '), 8)

    def test_count_cyrillic(self):
        self.assertEqual(count_cyrillic(''), 0)
        self.assertEqual(count_cyrillic('Hello, wёrld!'), 1)
        self.assertEqual(count_cyrillic('Привет'), 6)
        self.assertEqual(count_cyrillic('Hello'), 0)

    def test_count_digits(self):
        self.assertEqual(count_digits(''), 0)
        self.assertEqual(count_digits('Hello, wёrld!'), 0)
        self.assertEqual(count_digits('Привет'), 0)
        self.assertEqual(count_digits('Hello'), 0)
        self.assertEqual(count_digits(' абыр_валг 782 '), 3)
