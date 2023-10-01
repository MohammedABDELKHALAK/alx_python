import requests
import json
import sys


def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetch employee TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_data = response.json()

    # Prepare JSON data
    json_data = {"USER_ID": []}
    for task in todo_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        json_data["USER_ID"].append(task_data)

    # Save data to a JSON file
    filename = f"{user_id}.json"
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Data exported to {filename}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
