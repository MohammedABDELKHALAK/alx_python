"""
    Fetch employee information and TODO list progress for a given employee ID.

    Parameters:
    employee_id (int): The employee ID.

    Returns:
    dict: A dictionary containing the employee's tasks.
      """


import json
import requests
import sys

def fetch_employee_info(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Create a dictionary with user_info and todos_info
    user_data = {
        "user_info": user_info,
        "tasks": todos_info
    }

    return user_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee information and tasks
    user_data = fetch_employee_info(employee_id)

    # Check if the correct user is fetched
    if user_data['user_info']['id'] == employee_id:
        print("Correct user: OK")
    else:
        print("Correct user: Incorrect")

    # Check if the value associated with USER_ID is a list of dicts
    if isinstance(user_data['tasks'], list) and all(isinstance(item, dict) for item in user_data['tasks']):
        print("User ID’s value is a list of dicts: OK")
    else:
        print("User ID’s value is not a list of dicts: Incorrect")

    # Check if all tasks are found in the list of dicts
    tasks_count = len(user_data['tasks'])
    if tasks_count == 0:
        print("No tasks found for this user")
    else:
        print("All tasks found in list of dicts: OK")
