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

    # URLs for user and todos information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user and todos information from the URLs
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Create a dictionary to store the employee's tasks
    user_tasks = {"task_list": []}

    # Iterate through the todos and extract relevant information
    for todo in todos_info:
        task_info = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user_info["username"]
        }
        user_tasks["task_list"].append(task_info)

    return user_tasks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee information and tasks
    tasks_data = fetch_employee_info(employee_id)

    # Write the tasks to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(tasks_data, json_file, indent=4)

    print(f"Tasks for employee {employee_id} exported to {filename}")
