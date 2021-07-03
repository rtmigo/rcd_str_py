import functools
import sys
import unicodedata
import warnings


@functools.lru_cache()
def regex_category_pattern(category: str) -> str:
    return '[{}]'.format("".join([chr(i) for i in range(sys.maxunicode) if
                                  unicodedata.category(chr(i)) == category]))


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
