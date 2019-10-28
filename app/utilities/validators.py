import re


def validate_email(email):
    match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)  # noqa
    if match:
        return True
    else:
        return False


def validate_string(string_):
    if string_.isspace():
        return False
    else:
        return True
