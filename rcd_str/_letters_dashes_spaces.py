import re

from rcd_str._minimize import minimize_spaces


def keep_letters_dashes_spaces(txt: str) -> str:
    # оставляет только символы, допустимые в имени города: пробелы,
    # дефисы, буквы

    txt = txt.replace("_", " ")
    txt = " ".join(re.findall(r'[-\w ]+', txt))  # остались альфанумерикс
    txt = re.sub(r'\d', '', txt)  # удалили цифры

    # любая смесь пробелов и дефисов превращается в одиночный дефис
    # без пробелов рядом
    txt = re.sub(r'\s*-[\s-]*', '-', txt)
    txt = txt.strip('-')  # никаких дефисов по краям

    return minimize_spaces(txt)


