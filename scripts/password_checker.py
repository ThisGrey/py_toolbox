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

def get_non_empty_password():
    while True:
        password = getpass.getpass("Enter the password to check: ").strip()
        if password:
            return password
        else:
            print("Password cannot be empty or contain only spaces. Please try again.")

if __name__ == "__main__":
    while True:
        password = get_non_empty_password()
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")
        print(f"---------------------------")

        repeat = input("Do you want to check another password? (y/n): ").lower()
        if repeat != 'y':
            print("Exiting...")
            break
