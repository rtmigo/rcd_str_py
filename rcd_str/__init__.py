# SPDX-FileCopyrightText: (c) 2012-2022 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


from ._alnum import alphawords, alphanumerics, keepalnum, \
    words_and_numbers, join_words_and_numbers_upper
from ._camel_case import CamelCase, camelcase_concat_words
from ._other import *  # todo
from ._regex_category_patterns import RegexCat, regexLu, regexLl
from ._sentence_case import sentence_case
from ._minimize import minimize_spaces
from ._letters_dashes_spaces import keep_letters_dashes_spaces
from ._is import is_blank
from ._deprecated import capitalizeAfterNonword, keepLettersDashesSpaces, \
    minimizeSpaces, sentenceCase, splitWaN, simpleWaN
