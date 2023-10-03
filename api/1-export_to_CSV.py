import csv
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

    return user_info, todos_info

def export_to_csv(user_id, user_name, todos):
    """ Export TODOs to CSV """
    filename = f"{user_id}.csv"
    with open(filename, mode='r', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([user_id, user_name, str(todo['completed']), todo['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_info, todos_info = fetch_employee_info(employee_id)

    user_id = user_info['id']
    user_name = user_info['username']

    export_to_csv(user_id, user_name, todos_info)
    print(f"Tasks exported to {user_id}.csv")
