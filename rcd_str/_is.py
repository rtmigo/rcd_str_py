import re


def is_blank(text: str) -> bool:
    return re.fullmatch(r'\s*', text) is not None
