import warnings

from . import keep_letters_dashes_spaces, minimize_spaces, sentence_case
from ._alnum import words_and_numbers, join_words_and_numbers_upper
from ._other import capitalize_word_sequences


# noinspection PyPep8Naming
def capitalizeAfterNonword(txt: str) -> str:
    # obsolete since 2022-01
    warnings.warn("Use capitalize_word_sequences",
                  DeprecationWarning,
                  stacklevel=2)
    return capitalize_word_sequences(txt)


# noinspection PyPep8Naming
def keepLettersDashesSpaces(txt: str) -> str:
    warnings.warn("Use keep_letters_dashes_spaces", DeprecationWarning,
                  stacklevel=2)
    return keep_letters_dashes_spaces(txt)


# noinspection PyPep8Naming
def minimizeSpaces(text, keepNewlines=False):
    warnings.warn("Use minimize_spaces", DeprecationWarning, stacklevel=2)
    return minimize_spaces(text, keep_newlines=keepNewlines)


# noinspection PyPep8Naming
def sentenceCase(s):
    warnings.warn("Use sentence_case", DeprecationWarning, stacklevel=2)
    return sentence_case(s)


# noinspection PyPep8Naming
def splitWaN(text):
    # 2021-01
    warnings.warn("Use words_and_numbers", DeprecationWarning,
                  stacklevel=2)
    return words_and_numbers(text)


# noinspection PyPep8Naming
def simpleWaN(text):
    """Удаляет пунктуацию, минимизирует пробелы, переводит строку в верхний
    регистр. Используется для "грубого сравнения" строк."""
    warnings.warn("Use words_and_numbers_upper", DeprecationWarning,
                  stacklevel=2)  # 2021-01
    return join_words_and_numbers_upper(text)
