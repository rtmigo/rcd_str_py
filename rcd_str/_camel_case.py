# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import re
from typing import List


class CamelCase:
    __compiledRegex = None

    @staticmethod
    def __getRegex():
        # https://stackoverflow.com/questions/29916065/how-to-do-camelcase-split-in-python
        if CamelCase.__compiledRegex is None:
            CamelCase.__compiledRegex = re.compile(r'''
                # Find words in a string. Order matters!
                [A-Z]+(?=[A-Z][a-z]) | # upper case before a capitalized word
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
