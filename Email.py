import re


def is_valid_email(email):
    # Define a regular expression pattern for validating an email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    # Check if the input email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
print(is_valid_email("example@domain.com"))  # Output: True
print(is_valid_email("invalid-email@domain"))  # Output: False
print(is_valid_email("another.invalid.email.com"))  # Output: False
