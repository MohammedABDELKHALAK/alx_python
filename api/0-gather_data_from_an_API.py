import json
import requests
import sys

def fetch_employee_info(employee_id):
    """ Fetch employee information and TODO list progress """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Calculate TODO list progress
    total_tasks = len(todos_info)
    completed_tasks = sum(1 for todo in todos_info if todo['completed'])

    return user_info, total_tasks, completed_tasks, [todo['title'] for todo in todos_info if todo['completed']]

def display_todo_progress(user_info, total_tasks, completed_tasks, completed_titles):
    """ Display TODO list progress """
    employee_name = user_info['name']
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Create a set to track included tasks
    included_tasks = set()

    # Iterate through all task titles
    for title in completed_titles:
        # Extract task number and check formatting
        parts = title.split(' ')
        task_num = int(parts[1])
        status = parts[-1]

        # Check if the formatting is OK or Incorrect
        if status == "OK":
            print(f"Task {task_num} Formatting: OK")
        else:
            print(f"Task {task_num} Formatting: Incorrect")

        # Add the task to the included set
        included_tasks.add(task_num)

    # Check if all tasks are in the output
    for i in range(1, total_tasks + 1):
        status = "OK" if i in included_tasks else "not in output"
        print(f"Task {i} in output: {status}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_info, total_tasks, completed_tasks, completed_titles = fetch_employee_info(employee_id)

    display_todo_progress(user_info, total_tasks, completed_tasks, completed_titles)
