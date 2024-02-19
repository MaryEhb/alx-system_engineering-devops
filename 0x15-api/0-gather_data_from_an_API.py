#!/usr/bin/python3
"""0. Gather data from an API"""

import requests
import sys

if (sys.argv[1]):
    urlTODO = 'https://jsonplaceholder.typicode.com/todos?userId='
    urlUSER = 'https://jsonplaceholder.typicode.com/users?id='
    res = requests.get(urlTODO + sys.argv[1]).json()
    user = requests.get(urlUSER + sys.argv[1]).json()[0]
    completed = [obj for obj in res if obj['completed']]
    print('Employee {} is done with tasks({}/{}):'.format(user['name'],
                                                          len(completed),
                                                          len(res)))
    for todo in completed:
        print("\t{}".format(todo['title']))
