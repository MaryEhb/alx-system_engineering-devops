#!/usr/bin/python3
"""3. Dictionary of list of dictionaries"""


if __name__ == '__main__':
    import requests
    import sys
    import json

    urlTODO = 'https://jsonplaceholder.typicode.com/todos'
    urlUSER = 'https://jsonplaceholder.typicode.com/users'
    res = requests.get(urlTODO).json()
    users = requests.get(urlUSER).json()
    users_dict = {user['id']: user['username'] for user in users}
    data = {}

    for todo in res:
        id = todo.get('userId')
        user = users_dict.get(id)
        if todo.get('userId') in data:
            data[id].append({"task": todo.get('title'),
                             "completed": todo.get('completed'),
                             "username": user})
        else:
            data[id] = [{"task": todo.get('title'),
                         "completed": todo.get('completed'),
                         "username": user}]

    with open("todo_all_employees.json", 'w') as file:
        json.dump(data, file)
