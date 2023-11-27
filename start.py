import os

script_folder = "scripts"

script_mapping = {
    "1": "generate_password.py",
    "2": "password_checker.py",
    "3": "random_number.py",
    "4": "get_weather.py"
}

while True:
    print("Select an option:")
    print("1. Generate password")
    print("2. Check password strength")
    print("3. Generate random number")
    print("4. Get Weather")
    print("5. Exit")

    choice = input("Enter the option number: ")

    if choice == "5":
        print("Exiting...")
        break

    script_name = script_mapping.get(choice)

    if script_name:
        script_path = os.path.join(script_folder, script_name)
        if os.path.exists(script_path):
            try:
                exec(open(script_path).read())
            except Exception as e:
                print(f"Error running {script_name}: {e}")
        else:
            print(f"Script not found: {script_name}")
    else:
        print("Invalid option. Please enter a valid option.")
