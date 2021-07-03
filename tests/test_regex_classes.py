# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import re
import unittest

from rcd_str import RegexCat


class TestRegexClasses(unittest.TestCase):
    def test(self):
        m = re.search(f'{RegexCat.uppercase_letter}\\w+',
                      f'стиральная машина Вятка названа в честь города')
        self.assertEqual(
            m.group(0), 'Вятка')
