import random

def generate_random_number():
        try:
            min_value = int(input("Enter the minimum value: "))
            max_value = int(input("Enter the maximum value: "))
            random_number = random.randint(min_value, max_value)
            print(f"Generated Random Number: {random_number}")
            print(f"---------------------------")
        except ValueError as ve:
            print(f"Error: {ve}. Please enter valid numbers.")

if __name__ == "__main__":
    generate_random_number()