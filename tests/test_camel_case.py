# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import unittest

from rcd_str._camel_case import CamelCase, camelcase_concat_words


class TestCamelCase(unittest.TestCase):

    def test(self):
        self.assertListEqual(CamelCase.split("TitleCase"), ["Title", "Case"])
        self.assertListEqual(CamelCase.split("camelCase"), ["camel", "Case"])
        self.assertListEqual(CamelCase.split("userID"), ["user", "ID"])
        self.assertListEqual(CamelCase.split("two words"), ["two", "words"])
        self.assertListEqual(CamelCase.split("number1splitsID"),
                             ['number', '1', 'splits', 'ID'])

        print("camel case tested")

    def test_first(self):
        self.assertEqual(CamelCase.first("TitleCase"), "Title")
        self.assertEqual(CamelCase.first("camelCase"), "camel")
        self.assertEqual(CamelCase.first("userID"), "user")
        self.assertEqual(CamelCase.first("two words"), "two")
        self.assertEqual(CamelCase.first("number1splitsID"), 'number')
        self.assertEqual(CamelCase.first(" "), "")
        self.assertEqual(CamelCase.first(""), "")

        print("camel case tested")

    def test_combine(self):
        self.assertEqual(camelcase_concat_words(['ALPHA', 'BETA', 'GAMMA']),
                         'alphaBetaGamma')
        self.assertEqual(camelcase_concat_words(['ALPHA', 'BETA', 'GAMMA'],
                                                upper=True),
                         'AlphaBetaGamma')
        self.assertEqual(camelcase_concat_words(['AlphaBeta', 'Gamma', 'theta']),
                         'alphabetaGammaTheta')

