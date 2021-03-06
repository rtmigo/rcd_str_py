# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import re
import unicodedata
import warnings


def contains(word, alpha=False, upper=False, digit=False):
    for c in word:
        if alpha and c.isalpha(): return True
        if upper and c.isupper(): return True
        if digit and c.isdigit(): return True
    return False


def isASCII(s):
    return all(ord(c) < 128 for c in s)


def capitalize_word_sequences(txt: str) -> str:
    return re.sub(r'(<?\W)\w|^\w', lambda m: m.group(0).upper(), txt)




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
