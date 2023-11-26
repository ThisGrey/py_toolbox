while True:
    print("Select an option:")
    print("1. Generate password")
    print("2. Check password strength")
    print("3. Generate random number")
    print("4. Exit")

    choice = input("Enter the option number: ")

    if choice == "1":
        try:
            exec(open("generate_password.py").read())
        except Exception as e:
            print(f"Error running generate_password.py: {e}")
    elif choice == "2":
        try:
            exec(open("password_checker.py").read())
        except Exception as e:
            print(f"Error running password_checker.py: {e}")
    elif choice == "3":
        try:
            exec(open("random_number.py").read())
        except Exception as e:
            print(f"Error running random_number_generator.py: {e}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please enter a valid option.")
