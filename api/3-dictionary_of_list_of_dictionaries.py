import json
import requests

def check_user_info():
    """ Check if all users are in the student's JSON """
    # Load student's JSON from file
    with open('todo_all_employees.json', 'r') as file:
        student_json = json.load(file)

    # Fetch correct JSON from the API
    correct_json = requests.get(users_url).json()

    # Check if each correct user ID is in the student's JSON
    for correct_entry in correct_json:
        user_id = str(correct_entry['id'])
        if user_id not in student_json:
            print("User ID {} Found: Incorrect".format(user_id))
            return

    print("All users found: OK")

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    check_user_info()
