import re

def is_valid_phone(phone):
    return re.match(r"^\d{3}-\d{3}-\d{4}$", phone) is not None

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
