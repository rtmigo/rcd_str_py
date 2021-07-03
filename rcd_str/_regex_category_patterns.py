# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import functools
import re
import sys
import unicodedata
import warnings
from typing import Iterable


def _iter_by_cat(category: str) -> Iterable[str]:
    for i in range(sys.maxunicode):
        c = chr(i)
        if unicodedata.category(c) == category:
            yield c


@functools.lru_cache()
def regex_category_pattern(category: str) -> str:
    chars = "".join(_iter_by_cat(category))
    chars = re.escape(chars)
    return f'[{chars}]'


class _RegexCatMeta(type):
    # https://www.regular-expressions.info/unicode.html#category
    @property
    def lowercase_letter(cls) -> str:
        return regex_category_pattern("Ll")

    @property
    def uppercase_letter(cls) -> str:
        return regex_category_pattern("Lu")


class RegexCat(metaclass=_RegexCatMeta):
    pass


def regexLu():
    warnings.warn('Use RegexCat.uppercase_letter', DeprecationWarning)
    return regex_category_pattern("Lu")


def regexLl():
    warnings.warn('Use RegexCat.lowercase_letter', DeprecationWarning)
    return regex_category_pattern("Ll")
