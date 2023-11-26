import string
import getpass

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    symbol_criteria = any(char in string.punctuation for char in password)

    if length_criteria and uppercase_criteria and digit_criteria and symbol_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or digit_criteria or symbol_criteria):
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    password = getpass.getpass("Enter the password to check: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print(f"---------------------------")