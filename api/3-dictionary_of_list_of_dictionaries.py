import json
import requests
import sys

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

def add_empty_users(organized_data, user_ids):
    # Ensure all user IDs exist in the organized data
    for user_id in user_ids:
        if user_id not in organized_data:
            organized_data[user_id] = []

def export_to_json(organized_data):
    # Save data to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(organized_data, file, indent=4)

    print(f"Data exported to {filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    todo_data = fetch_todo_data()
    organized_data = organize_data([task for task in todo_data if task['userId'] == int(user_id)])

    # Extract unique user IDs
    user_ids = set(task['userId'] for task in todo_data)

    add_empty_users(organized_data, user_ids)
    export_to_json(organized_data)