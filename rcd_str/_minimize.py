import warnings


def minimize_spaces(text, keep_newlines=False) -> str:
    if keep_newlines:
        lines = text.split("\n")
        lines = (minimize_spaces(line, keep_newlines=False) for line in lines)
        return "\n".join(lines)
    else:
        return " ".join(text.split())


def minimizeSpaces(text, keepNewlines=False):
    warnings.warn("Use minimize_spaces", DeprecationWarning)
    return minimize_spaces(text, keep_newlines=keepNewlines)
