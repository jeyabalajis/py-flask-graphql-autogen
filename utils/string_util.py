import string


def to_camel_case(s: str, init_caps=False) -> str:
    return (s[0].upper() if init_caps else s[0].lower()) + string.capwords(s, sep='_').replace('_', '')[1:] if s else s
