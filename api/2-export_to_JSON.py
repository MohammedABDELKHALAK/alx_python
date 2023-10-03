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
