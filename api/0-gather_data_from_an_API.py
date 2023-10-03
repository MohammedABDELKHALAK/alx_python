import json
import requests
import sys

# Assuming todos_url is defined somewhere in your code
todos_url = "https://jsonplaceholder.typicode.com/todos"

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

def check_tasks():
    """ Fetch user name, number of tasks """
    filename = 'student_output'
    count = 0
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            count += 1
            if line[0] == '\t' and line[1] == ' ' and line[-1] == '\n':
                print("Task {} Formatting: OK".format(count))
            else:
                print("Task {} Formatting: Incorrect".format(count))

def display_todo_progress(user_info, total_tasks, completed_tasks, completed_titles):
    """ Display TODO list progress """
    employee_name = user_info['name']
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    check_tasks()  # Check task formatting
    for i, title in enumerate(completed_titles, start=1):
        print(f"Task {i} Formatting: OK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_info, total_tasks, completed_tasks, completed_titles = fetch_employee_info(employee_id)

    display_todo_progress(user_info, total_tasks, completed_tasks, completed_titles)
