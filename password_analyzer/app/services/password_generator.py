import string
import secrets

def generate_password(length: int = 12, include_uppercase: bool = True, 
                      include_lowercase: bool = True, include_numbers: bool = True, 
                      include_special: bool = True):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    character_set = ''
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_numbers:
        character_set += string.digits
    if include_special:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be included.")

    # Generate password
    password = ''.join(secrets.choice(character_set) for _ in range(length))

    # Ensure all requested character types are included
    if include_lowercase and not any(c.islower() for c in password):
        password = replace_random_char(password, string.ascii_lowercase)
    if include_uppercase and not any(c.isupper() for c in password):
        password = replace_random_char(password, string.ascii_uppercase)
    if include_numbers and not any(c.isdigit() for c in password):
        password = replace_random_char(password, string.digits)
    if include_special and not any(c in string.punctuation for c in password):
        password = replace_random_char(password, string.punctuation)

    return password

def replace_random_char(password, char_set):
    index = secrets.randbelow(len(password))
    return password[:index] + secrets.choice(char_set) + password[index+1:]