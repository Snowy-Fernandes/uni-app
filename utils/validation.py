import re

EMAIL_PATTERN = r"^[a-z]+\.[a-z]+@university\.com$"
PASSWORD_PATTERN = r"^[A-Z][a-zA-Z]{4,}\d{3,}$"


def is_valid_email(email):
    return re.match(EMAIL_PATTERN, email, re.IGNORECASE) is not None


def is_valid_password(password):
    return re.match(PASSWORD_PATTERN, password) is not None
