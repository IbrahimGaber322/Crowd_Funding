# user_module.py


import re

users = {}

def load_users():
    with open("users.txt", "r") as f:
        for line in f:
            email, first_name, last_name, password, phone = line.strip().split(",")
            users[email] = {
                'first_name': first_name,
                'last_name': last_name,
                'password': password,
                'phone': phone
            }

def register():
    first_name = input("Enter your first name: ")
    if not validate_input(first_name, "First Name", r'^[a-zA-Z]+$'):
        return
    last_name = input("Enter your last name: ")
    if not validate_input(last_name, "Last Name", r'^[a-zA-Z]+$'):
        return
    email = input("Enter your email: ")
    if not validate_input(email, "Email", r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'):
        return
    if email in users:
        print("Email already exists. Please choose a different email.")
        return
    password = input("Enter your password: ")
    if not validate_input(password, "Password") or len(password) < 8 or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
        print("Password must be at least 8 characters long and contain at least one uppercase letter and one number.")
        return
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    phone = input("Enter your mobile phone number: ")
    if not validate_input(phone, "Phone Number", r'^01[0-2]\d{8}$'):
        return
    users[email] = {
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'phone': phone
    }
    with open("users.txt", "a") as f:
        f.write(f"{email},{first_name},{last_name},{password},{phone}\n")
    print("Registration successful.")

def login():
    global user
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email in users and users[email]['password'] == password:
        print("Login successful.")
        return email
    else:
        print("Invalid email, password. Please try again.")
        return None

def logout():
    print("Logged out successfully.")
    return None

def validate_input(value, field_name, regex=None):
    if not value.strip():
        print(f"{field_name} cannot be empty. Please try again.")
        return False
    if regex and not re.match(regex, value):
        print(f"Invalid {field_name}. Please try again.")
        return False
    return True
