
import warnings

from . import keep_letters_dashes_spaces, minimize_spaces, sentence_case
from ._other import capitalize_word_sequences

# noinspection PyPep8Naming
def capitalizeAfterNonword(txt: str) -> str:
    # obsolete since 2022-01
    warnings.warn("Use capitalize_word_sequences", DeprecationWarning)
    return capitalize_word_sequences(txt)


def keepLettersDashesSpaces(txt: str) -> str:
    warnings.warn("Use keep_letters_dashes_spaces", DeprecationWarning)
    return keep_letters_dashes_spaces(txt)


def minimizeSpaces(text, keepNewlines=False):
    warnings.warn("Use minimize_spaces", DeprecationWarning)
    return minimize_spaces(text, keep_newlines=keepNewlines)


def sentenceCase(s):
    warnings.warn("Use sentence_case", DeprecationWarning)
    return sentence_case(s)