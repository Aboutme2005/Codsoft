import random
import string

def display_menu():
    print("\nPassword Generator")
    print("1. Generate Password")
    print("2. Exit")

def generate_password():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
        
        # Define the characters for the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            generate_password()
        elif choice == '2':
            print("Exiting Password Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        
        
        
