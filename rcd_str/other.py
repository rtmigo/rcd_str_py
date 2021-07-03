import re
import unicodedata
import unittest
from pathlib import Path
from typing import List, Union, Optional


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


def keepalnum(txt):
    import re
    # http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    pattern = re.compile('[\W_]+')
    return pattern.sub('', txt)


class TestKeepAlnum(unittest.TestCase):
    def test(self):
        self.assertEqual(
            keepalnum("  Мир! Дружба! Жвачка! Олимпиада 1980! x86_64  "),
            "МирДружбаЖвачкаОлимпиада1980x8664")


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

def splitWaN(text):
    return alphanumerics(text, underscore=False, separateNumbers=True)


#	if undercore:
#		expr = r"[^\W\d]+|\d+"
#	else:
#		expr = r"[^\W\d_]+|\d+"

#	return re.findall(expr, text)

def alphanumerics(text, underscore=False, separateNumbers=False):
    # \w		буква, цифра или "_"
    # \W		всё, кроме "\w". То есть, не буква, не цифра и не подчеркивание
    # [^\W]		отрицание \W экваивалентно отрицанию отрицания \w, то есть эквивалентно \w
    # [^\W_]	"\w", но не "_"

    if separateNumbers:
        if underscore:
            return re.findall(r"[^\W\d]+|\d+", text)
        else:
            return re.findall(r"[^\W\d_]+|\d+", text)
    else:
        if underscore:
            return re.findall(r"\w+", text)  # ?! не тестировано!
        else:
            return re.findall(r"[^\W_]+", text)  # ?! не тестировано!


def alphawords(text, underscore=False):
    if underscore:
        return re.findall(r"[^\W_]+", text)
    else:
        return re.findall(r"[^\W\d_]+", text)


import unittest


class Test519(unittest.TestCase):
    def test_alphawords(self):
        assert alphawords("number 1 and number 2 are numbers") == ['number',
                                                                   'and',
                                                                   'number',
                                                                   'are',
                                                                   'numbers']
        assert alphawords(
            "Here is undercore_glued_ident and '20' in quotes ") == ['Here',
                                                                     'is',
                                                                     'undercore',
                                                                     'glued',
                                                                     'ident',
                                                                     'and',
                                                                     'in',
                                                                     'quotes']


def keepLettersDashesSpaces(txt: str) -> str:
    # оставляет только символы, допустимые в имени города: пробелы, дефисы, буквы

    txt = txt.replace("_", " ")
    txt = " ".join(re.findall('''[-\w ]+''', txt))  # остались альфанумерикс
    txt = re.sub('''\d''', '', txt)  # удалили цифры

    # любая смесь пробелов и дефисов превращается в одиночный дефис без пробелов рядом
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


def simpleWaN(text):
    """для приблизительного сравнения строк. Удаляет пунктуацию, минимизирует
    пробелы, переводит строку в верхний регистр."""
    return " ".join(splitWaN(text.upper()))


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


def sentenceCase(s):
    i = None

    for i, c in enumerate(s):
        if c.isalpha():
            break

    if i is None:
        return s

    return s[:i] + s[i].upper() + s[i + 1:]


class TestSentenceCase(unittest.TestCase):

    def test(self):
        self.assertEqual(sentenceCase("иван"), "Иван")
        self.assertEqual(sentenceCase("иван Евгеньевич Смирнов"),
                         "Иван Евгеньевич Смирнов")
        self.assertEqual(sentenceCase("красный богатырь"), "Красный богатырь")

        self.assertEqual("«шербурские зонтики»".capitalize(),
                         "«шербурские зонтики»")
        self.assertEqual(sentenceCase("«шербурские зонтики»"),
                         "«Шербурские зонтики»")
        self.assertEqual(sentenceCase("«the Beatles»"), "«The Beatles»")

        self.assertEqual(sentenceCase(""), "")
        self.assertEqual(sentenceCase("1"), "1")
        self.assertEqual(sentenceCase("123"), "123")
        self.assertEqual(sentenceCase("1x"), "1X")
        self.assertEqual(sentenceCase("x"), "X")


# TestSentenceCase().test_pershi()
# exit()


# TestWild().test_wildMatch()

# print(wildFullMatch("zzz", "Текст. * Лала"))
# exit()

##############################################################################

class CamelCase:
    __compiledRegex = None

    @staticmethod
    def __getRegex():
        # https://stackoverflow.com/questions/29916065/how-to-do-camelcase-split-in-python
        if CamelCase.__compiledRegex is None:
            CamelCase.__compiledRegex = re.compile(r'''
				# Find words in a string. Order matters!
				[A-Z]+(?=[A-Z][a-z]) |  # All upper case before a capitalized word
				[A-Z]?[a-z]+ |  # Capitalized words / all lower case
				[A-Z]+ |  # All upper case
				\d+  # Numbers
			''', re.VERBOSE | re.MULTILINE)
        return CamelCase.__compiledRegex

    @staticmethod
    def split(txt: str) -> List[str]:
        return CamelCase.__getRegex().findall(txt)

    @staticmethod
    def first(txt: str) -> str:
        m = CamelCase.__getRegex().search(txt)
        if m:
            return m.group()
        else:
            return ""

    @staticmethod
    def _firstNaive(text) -> str:

        import warnings

        warnings.warn("Deprecated", DeprecationWarning)

        result = ""

        isFirst = True
        for c in text:
            if c.isalpha() and (isFirst or not c.isupper()):
                result += c
            else:
                break
            isFirst = False

        return result

