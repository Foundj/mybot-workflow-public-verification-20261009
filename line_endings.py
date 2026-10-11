def normalize_line_endings(value):
    if not isinstance(value, str):
        raise TypeError("normalize_line_endings expects str")
    return value.replace("\r\n", "\n").replace("\r", "\n")
