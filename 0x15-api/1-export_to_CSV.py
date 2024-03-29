#!/usr/bin/python3
"""1. Export to CSV"""


if __name__ == '__main__':
    import requests
    import sys
    import csv

    if (sys.argv[1]):
        urlTODO = 'https://jsonplaceholder.typicode.com/todos?userId='
        urlUSER = 'https://jsonplaceholder.typicode.com/users?id='
        res = requests.get(urlTODO + sys.argv[1]).json()
        user = requests.get(urlUSER + sys.argv[1]).json()[0]
        completed = [obj for obj in res if obj.get('completed')]

        with open("{}.csv".format(user.get('id')), 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in res:
                writer.writerow([todo.get('userId'),
                                 user.get('username'),
                                 todo.get('completed'),
                                 todo.get('title')])
