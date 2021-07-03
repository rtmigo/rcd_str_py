# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import warnings


def sentence_case(text: str) -> str:
    i = None

    for i, c in enumerate(text):
        if c.isalpha():
            break

    if i is None:
        return text

    return text[:i] + text[i].upper() + text[i + 1:]


def sentenceCase(s):
    warnings.warn("Use sentence_case", DeprecationWarning)
    return sentence_case(s)
