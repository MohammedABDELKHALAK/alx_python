import requests
import csv
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

    # Prepare CSV data
    csv_data = []
    for task in todo_data:
        task_completed_status = "completed" if task['completed'] else "not completed"
        task_title = task['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

    # Save data to a CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)

    print(f"Data exported to {filename}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
