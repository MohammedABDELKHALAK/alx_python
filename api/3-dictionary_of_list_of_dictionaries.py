import requests
import json


def fetch_todo_data():
    # Fetch TODO data for all users
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todo_url)
    todo_data = response.json()
    return todo_data


def organize_data(todo_data):
    # Organize data in the specified JSON format
    organized_data = {}

    for task in todo_data:
        user_id = task['userId']
        username = task['username']
        task_data = {
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        }

        if user_id not in organized_data:
            organized_data[user_id] = []
        organized_data[user_id].append(task_data)

    return organized_data


def export_to_json(organized_data):
    # Save data to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(organized_data, file, indent=4)

    print(f"Data exported to {filename}.")


if __name__ == "__main__":
    todo_data = fetch_todo_data()
    organized_data = organize_data(todo_data)
    export_to_json(organized_data)
