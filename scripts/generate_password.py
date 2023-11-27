import random
import string
import pyperclip

def generate_password(length=12, include_symbols=False):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!$%&()*+,-./:;<=>?@[\\]^_`{|}~" if include_symbols else ""
    
    all_characters = letters + digits + symbols
    password = ''.join(random.choice(all_characters) for c in range(length))
    
    print(f"Generated Password: {password}")
    
    add_to_clipboard = input("Do you want to add this password to the clipboard? (y/n): ").lower()
    if add_to_clipboard == 'y':
        pyperclip.copy(password)
        print("Password added to the clipboard.")
    else:
        print("Password not added to the clipboard.")

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    generate_password(length, include_symbols)
    print(f"---------------------------")
