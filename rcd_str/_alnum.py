import re
from typing import List


def alphanumerics(text,
                  underscore=False,
                  separate_numbers=False):
    # todo test

    # \w		буква, цифра или "_"
    # \W		всё, кроме "\w". То есть, не буква, не цифра и не подчеркивание
    # [^\W]		отрицание \W экваивалентно отрицанию отрицания \w,
    #           то есть эквивалентно \w
    # [^\W_]	"\w", но не "_"

    if separate_numbers:
        if underscore:
            return re.findall(r"[^\W\d]+|\d+", text)
        else:
            return re.findall(r"[^\W\d_]+|\d+", text)
    else:
        if underscore:
            return re.findall(r"\w+", text)  # ?! не тестировано!
        else:
            return re.findall(r"[^\W_]+", text)  # ?! не тестировано!


def alphawords(text: str, underscore: bool = False) -> List[str]:
    """Returns all alpha character sequences from the `text`.

    If `underscore` is True, the '_' is also treated as an alpha character.
    """
    if underscore:
        return re.findall(r"[^\W\d]+", text)
    else:
        return re.findall(r"[^\W\d_]+", text)


def keepalnum(txt: str) -> str:
    # http://stackoverflow.com/questions/1276764/
    # stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    pattern = re.compile(r'[\W_]+')
    return pattern.sub('', txt)


def words_and_numbers(text: str) -> List[str]:
    return alphanumerics(text, underscore=False, separate_numbers=True)


def join_words_and_numbers_upper(text: str) -> str:
    """Удаляет пунктуацию, минимизирует пробелы, переводит строку в верхний
    регистр. Используется для "грубого сравнения" строк."""
    return " ".join(words_and_numbers(text.upper()))
