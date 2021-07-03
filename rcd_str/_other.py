# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import re
import unicodedata
import unittest
from pathlib import Path
from typing import Union, Optional


class LazyRegex:

    def __init__(self, source: Union[str, Path], flags: int):
        if source is None:
            raise ValueError
        self.source: Optional[Union[str, Path]] = source
        self._rx: Optional[re.Pattern] = None
        self._flags = flags

    @property
    def compiled(self) -> re.Pattern:

        if isinstance(self.source, Path):
            pattern = self.source.read_text()
        else:
            assert self.source is not None
            pattern = self.source

        if self._rx is None:
            self._rx = re.compile(pattern, self._flags)
            self.source = None

        return self._rx


def contains(word, alpha=False, upper=False, digit=False):
    for c in word:
        if alpha and c.isalpha(): return True
        if upper and c.isupper(): return True
        if digit and c.isdigit(): return True
    return False


def isASCII(s):
    return all(ord(c) < 128 for c in s)




def capitalizeAfterNonword(txt: str) -> str:
    return re.sub('(<?\W)\w|^\w', lambda m: m.group(0).upper(), txt)


class TestCapita(unittest.TestCase):
    def test(self):
        self.assertEqual(capitalizeAfterNonword('усть-каменогорск'),
                         'Усть-Каменогорск')
        self.assertEqual(capitalizeAfterNonword('нижний тагил'), 'Нижний Тагил')


# TestKeepAlnum().test()
# exit()

#########
#   splitWan:       "some123text, and something" -> "some", "123", "text", "and", "something"
#   alphanumerics:  "some123text, and something" -> "some123text", "and", "something"


#	if undercore:
#		expr = r"[^\W\d]+|\d+"
#	else:
#		expr = r"[^\W\d_]+|\d+"

#	return re.findall(expr, text)




def keepLettersDashesSpaces(txt: str) -> str:
    # оставляет только символы, допустимые в имени города: пробелы,
    # дефисы, буквы

    txt = txt.replace("_", " ")
    txt = " ".join(re.findall('''[-\w ]+''', txt))  # остались альфанумерикс
    txt = re.sub('''\d''', '', txt)  # удалили цифры

    # любая смесь пробелов и дефисов превращается в одиночный дефис
    # без пробелов рядом
    txt = re.sub('''\s*-[\s-]*''', '-', txt)
    txt = txt.strip('-')  # никаких дефисов по краям

    return minimizeSpaces(txt)


class TestKeepLetters(unittest.TestCase):

    def test(self):
        self.assertEqual(keepLettersDashesSpaces("Санкт-Петербург"),
                         "Санкт-Петербург")

        self.assertEqual(keepLettersDashesSpaces("-Узда-"), "Узда")
        self.assertEqual(keepLettersDashesSpaces("- Узда -"), "Узда")

        self.assertEqual(keepLettersDashesSpaces("Усть---Каменогорск"),
                         "Усть-Каменогорск")
        self.assertEqual(keepLettersDashesSpaces("Усть - --- Каменогорск"),
                         "Усть-Каменогорск")

        self.assertEqual(keepLettersDashesSpaces("Космонавтов, 6"),
                         "Космонавтов")

        self.assertEqual(keepLettersDashesSpaces(":) Нижний__Тагил!!!"),
                         "Нижний Тагил")
        self.assertEqual(keepLettersDashesSpaces("  Красная\t\tПоляна "),
                         "Красная Поляна")
        self.assertEqual(keepLettersDashesSpaces("Красная Поляна"),
                         "Красная Поляна")
        self.assertEqual(keepLettersDashesSpaces("Кривой   Рог"), "Кривой Рог")
        self.assertEqual(keepLettersDashesSpaces("Кривой_Рог"), "Кривой Рог")


# update(alphawords("number 1 and number 2 are numbers"))
#	exit()


# test_alphas()
# exit()


def minimizeSpaces(text, keepNewlines=False):
    if keepNewlines:
        lines = text.split("\n")
        lines = [minimizeSpaces(line, keepNewlines=False) for line in lines]
        return "\n".join(lines)
    else:
        return " ".join(text.split())


def alphabet(startLetter, endLetter):
    return "".join(chr(i) for i in range(ord(startLetter), ord(endLetter) + 1))


def isLetter(c):
    cat = unicodedata.category(c)
    return cat == "Ll" or cat == "Lu"


def isUppercaseLetter(c):
    return unicodedata.category(c) == "Lu"


def isLowercaseLetter(c):
    return unicodedata.category(c) == "Lu"


def unicodeLetters(uppercase=None):
    all_unicode = ''.join(chr(i) for i in range(65536))

    if uppercase is None:
        lst = []
        for c in all_unicode:
            cat = unicodedata.category(c)
            if cat == "Ll" or cat == "Lu":
                lst.append(c)
    elif uppercase:
        lst = [c for c in all_unicode if unicodedata.category(c) == 'Lu']
    else:
        lst = [c for c in all_unicode if unicodedata.category(c) == 'Ll']

    return ''.join(lst)


def findAll(big, sub, start=0, end=None):
    # if end is None:
    #	end=len(big)-len(sub)+1
    while True:
        idx = big.find(sub, start)
        if idx == -1:
            break
        yield idx
        start = idx + 1


def reFind(text, pattern):
    result = re.search(pattern, text)
    if result is None:
        return None
    else:
        return result.group()


def stripHtml(htmlCode, tagsReplacement=""):
    return re.sub(r'<[^>]+>', tagsReplacement, htmlCode)


def wildFullMatch(text: str, wildcard: str) -> bool:
    wildcard = re.escape(wildcard)
    wildcard = wildcard.replace("\\*", ".*")
    # wildcard = "^"+wildcard+"$"

    # print(re.fullmatch(wildcard, text, re.MULTILINE|re.DOTALL))

    return re.fullmatch(wildcard, text, re.MULTILINE | re.DOTALL) is not None


# print(wildcard)


