# project_module.py

from datetime import datetime
import re

projects = []


def load_projects():
    with open("projects.txt", "r") as f:
        for line in f:
            title, details, target, start_date_str, end_date_str, owner = line.strip().split(",")
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            projects.append({
                'title': title,
                'details': details,
                'target': int(target),
                'start_date': start_date,
                'end_date': end_date,
                'owner': owner
            })


def create_project(user):
    if not user:
        print("Please login first.")
        return

    title = input("Enter project title: ")
    if not validate_input(title, "Title"):
        return

    details = input("Enter project details: ")
    if not validate_input(details, "Details"):
        return

    target = input("Enter total target amount: ")
    try:
        target = int(target)
        if target <= 0:
            raise ValueError
    except ValueError:
        print("Invalid target amount. Please enter a positive integer.")
        return

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if start_date >= end_date:
        print("End date must be after start date. Please try again.")
        return

    with open("projects.txt", "a") as f:
        f.write(f"{title},{details},{target},{start_date.strftime(
            '%Y-%m-%d')},{end_date.strftime('%Y-%m-%d')},{user}\n")
    load_projects()
    print("Project created successfully.")


def view_projects():
    for idx, project in enumerate(projects, start=1):
        print(f"Project {idx}:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['target']}")
        print(f"Start Date: {project['start_date'].strftime('%Y-%m-%d')}")
        print(f"End Date: {project['end_date'].strftime('%Y-%m-%d')}")
        print(f"Owner: {project['owner']}")
        print()


def edit_project(user):
    if not user:
        print("Please login first.")
        return

    view_projects()
    project_number = input("Enter the project number you want to edit: ")
    try:
        project_number = int(project_number)
        if project_number < 1 or project_number > len(projects):
            raise ValueError
    except ValueError:
        print("Invalid project number. Please try again.")
        return

    project = projects[project_number - 1]
    if project['owner'] != user:
        print("You can only edit your own projects.")
        return

    title = input(
        "Enter new project title (leave blank to keep the current title): ")
    details = input(
        "Enter new project details (leave blank to keep the current details): ")
    target = input(
        "Enter new total target amount (leave blank to keep the current target): ")
    start_date = input(
        "Enter new start date (YYYY-MM-DD) (leave blank to keep the current start date): ")
    end_date = input(
        "Enter new end date (YYYY-MM-DD) (leave blank to keep the current end date): ")

    project['title'] = title if title else project['title']
    project['details'] = details if details else project['details']
    if target:
        try:
            project['target'] = int(target)
        except ValueError:
            print("Invalid target amount. Target amount remains unchanged.")
    project['start_date'] = datetime.strptime(
        start_date, '%Y-%m-%d') if start_date else project['start_date']
    project['end_date'] = datetime.strptime(
        end_date, '%Y-%m-%d') if end_date else project['end_date']

    with open("projects.txt", "w") as f:
        for project in projects:
            f.write(f"{project['title']},{project['details']},{project['target']},{project['start_date'].strftime(
                '%Y-%m-%d')},{project['end_date'].strftime('%Y-%m-%d')},{project['owner']}\n")
    print("Project edited successfully.")


def delete_project(user):
    if not user:
        print("Please login first.")
        return

    view_projects()
    project_number = input("Enter the project number you want to delete: ")
    try:
        project_number = int(project_number)
        if project_number < 1 or project_number > len(projects):
            raise ValueError
    except ValueError:
        print("Invalid project number. Please try again.")
        return

    project = projects[project_number - 1]
    if project['owner'] != user:
        print("You can only delete your own projects.")
        return

    del projects[project_number - 1]

    with open("projects.txt", "w") as f:
        for project in projects:
            f.write(f"{project['title']},{project['details']},{project['target']},{project['start_date'].strftime(
                '%Y-%m-%d')},{project['end_date'].strftime('%Y-%m-%d')},{project['owner']}\n")
    print("Project deleted successfully.")


def validate_input(value, field_name, regex=None):
    if not value.strip():
        print(f"{field_name} cannot be empty. Please try again.")
        return False
    if regex and not re.match(regex, value):
        print(f"Invalid {field_name}. Please try again.")
        return False
    return True
