import json
import os

# File to store passwords
PASSWORD_FILE = 'password.json'

def load_passwords():
    # Load the passwords from the JSON file.
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    # Save the password to JSON file.
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

def add_password(website, username, password):
    # Add a new password to the manager
    passwords = load_passwords()
    passwords[website] = {'username': username, 'password': password}
    save_passwords(passwords)
    print(f"Password for {website} added.")

def get_password(website):
    # Retrieve password by website name
    passwords = load_passwords()
    if website in passwords:
        print(f'Website: {website}')
        print(f'Username: {passwords[website]["username"]}')
        print(f'Password: {passwords[website]["password"]}')
    else:
        print(f'No account found for {website}.')

def main():
    while True:
        print('\nPassword Manager')
        print('1. Add a new password')
        print('2. Retrieve a password')
        print('3. Exit')
        choice = input("Choose an option: ")

        if choice == '1':
            website = input("Enter the name of the website name: ")
            username= input("Enter username: ")
            password = input("Enter the password: ")
            add_password(website, username, password)
        elif choice == '2':
            website = input("Enter the name of the website: ")
            get_password(website)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()