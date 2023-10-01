import json
import requests

def fetch_user_tasks():
    """ Fetch tasks for all users """
    users = requests.get(users_url).json()
    tasks_by_user = {}

    # Fetch tasks for each user
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        tasks = requests.get(todos_url, params={'userId': user_id}).json()

        # Add tasks for the user
        tasks_by_user[user_id] = []
        for task in tasks:
            task_info = {
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            }
            tasks_by_user[user_id].append(task_info)

    return tasks_by_user

def save_to_json(data, filename):
    """ Save data to a JSON file """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    # Fetch tasks for all users
    tasks_by_user = fetch_user_tasks()

    # Save the data to JSON file
    save_to_json(tasks_by_user, 'todo_all_employees.json')
    print('Data exported to todo_all_employees.json')
