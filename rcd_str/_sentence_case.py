# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


def sentence_case(text: str) -> str:
    i = None

    for i, c in enumerate(text):
        if c.isalpha():
            break

    if i is None:
        return text

    return text[:i] + text[i].upper() + text[i + 1:]


