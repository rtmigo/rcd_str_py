def minimize_spaces(text: str, keep_newlines=False) -> str:
    if keep_newlines:
        return "\n".join(
            (minimize_spaces(line, keep_newlines=False)
             for line in text.split("\n")))
    else:
        return " ".join(text.split())


def remove_empty_lines(text: str) -> str:
    return "\n".join([line for line in text.splitlines() if line])
