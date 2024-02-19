#!/usr/bin/python3
"""2. Export to JSON"""


if __name__ == '__main__':
    import requests
    import sys
    import json

    if (sys.argv[1]):
        urlTODO = 'https://jsonplaceholder.typicode.com/todos?userId='
        urlUSER = 'https://jsonplaceholder.typicode.com/users?id='
        res = requests.get(urlTODO + sys.argv[1]).json()
        user = requests.get(urlUSER + sys.argv[1]).json()[0]
        completed = [obj for obj in res if obj.get('completed')]
        data = {user.get('id'): [{"task": todo.get('title'),
                                  "completed": todo.get('completed'),
                                  "username": user.get('username')
                                  } for todo in res]}

        with open("{}.json".format(user.get('id')), 'w') as file:
            json.dump(data, file)
