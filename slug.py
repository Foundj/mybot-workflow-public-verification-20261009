def normalize_slug(value):
    if not isinstance(value, str):
        raise TypeError("normalize_slug expects str")
    return "-".join(value.split()).lower()
