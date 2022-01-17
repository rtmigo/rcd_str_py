import unittest

from rcd_str import keepalnum, alphawords


class TestKeepAlnum(unittest.TestCase):
    def test_keepalnum(self):
        self.assertEqual(
            keepalnum("  Мир! Дружба! Жвачка! Олимпиада 1980! x86_64  "),
            "МирДружбаЖвачкаОлимпиада1980x8664")


class TestAlphaWords(unittest.TestCase):
    def test_alphawords(self):
        self.assertListEqual(
            alphawords("number 1 and number 2 are numbers"),
            ['number', 'and', 'number', 'are', 'numbers'])

    def test_underscore(self):
        self.assertListEqual(
            alphawords("Here is undercore_glued_ident and '20' in quotes "),
            ['Here', 'is', 'undercore', 'glued', 'ident', 'and', 'in',
             'quotes'])

        self.assertListEqual(
            alphawords("Here is undercore_glued_ident and '20' in quotes ",
                       underscore=True),
            ['Here', 'is', 'undercore_glued_ident', 'and', 'in',
             'quotes'])
