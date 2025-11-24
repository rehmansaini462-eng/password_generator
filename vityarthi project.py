# PASSWORD GENERATOR PROJECT
import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    all_chars = lower + upper + numbers + special

    if length < 4:  # Minimum length for variety
        return "Password length should be at least 4 characters."

    # Ensure at least one character from each selected type
    password = [random.choice(lower)]
    if use_uppercase:
        password.append(random.choice(upper))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special))

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to avoid predictability
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == '__main__':
    print("Generated Password:", generate_password(12))
