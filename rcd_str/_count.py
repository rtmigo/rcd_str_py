import re


def _count_re(expr: str, text: str) -> int:
    return sum(len(s) for s in re.findall(expr, text))


def count_letters(text: str) -> int:
    return _count_re(r'[^\W\d_]+', text)


def count_digits(text: str) -> int:
    return _count_re(r'\d+', text)


def count_cyrillic(text: str) -> int:
    return _count_re(r'[\u0400-\u04FF]+', text)
