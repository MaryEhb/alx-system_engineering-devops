#!/usr/bin/python3
"""0. Gather data from an API"""


if __name__ == '__main__':
    import requests
    import sys

    if (sys.argv[1]):
        urlTODO = 'https://jsonplaceholder.typicode.com/todos?userId='
        urlUSER = 'https://jsonplaceholder.typicode.com/users/'
        res = requests.get(urlTODO + sys.argv[1]).json()
        user = requests.get(urlUSER + sys.argv[1]).json()
        completed = [obj for obj in res if obj.get('completed')]
        print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
                                                              len(completed),
                                                              len(res)))
        for todo in completed:
            print("\t {}"i.format(todo.get('title')))
