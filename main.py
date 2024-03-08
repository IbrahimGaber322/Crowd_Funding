# main.py

import os
from datetime import datetime
from user_module import load_users, register, login, logout
from project_module import load_projects, create_project, view_projects, edit_project, delete_project

user = None


def logged_out_menu():
    print("\n1. Register\n2. Login\n3. Exit")


def logged_in_menu():
    print("\n1. Create Project\n2. Edit Project\n3. Delete Project\n4. View Projects\n5. Logout\n6. Exit")


if __name__ == "__main__":
    # Check if users.txt and projects.txt exist, create if they don't
    if not os.path.exists("users.txt"):
        create_users_file = input(
            "users.txt does not exist. Do you want to create it? (yes/no): ")
        if create_users_file.lower() == "yes":
            with open("users.txt", "w") as f:
                pass
        else:
            print("Exiting application.")
            exit()

    if not os.path.exists("projects.txt"):
        create_projects_file = input(
            "projects.txt does not exist. Do you want to create it? (yes/no): ")
        if create_projects_file.lower() == "yes":
            with open("projects.txt", "w") as f:
                pass
        else:
            print("Exiting application.")
            exit()

    load_users()
    load_projects()

    while True:
        if user is None:
            logged_out_menu()
        else:
            logged_in_menu()

        choice = input("Enter your choice: ")

        if user is None:
            if choice == '1':
                register()
            elif choice == '2':
                user = login()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            if choice == '1':
                create_project(user)
            elif choice == '2':
                edit_project(user)
            elif choice == '3':
                delete_project(user)
            elif choice == '4':
                view_projects()
            elif choice == '5':
                user = logout()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    print("Exiting application.")
