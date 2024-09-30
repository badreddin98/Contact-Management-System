import re

def is_valid_phone(phone):
    return re.match(r"^\d{3}-\d{3}-\d{4}$", phone) is not None

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    
def validate_unique_id(unique_id):
    return re.match(r"[^@]+@[^@]+\.[^@]+", unique_id) or re.match(r"^\d{3}-\d{3}-\d{4}$", unique_id) is not None