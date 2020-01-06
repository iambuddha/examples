#!/usr/local/bin/python3.8

user = [{ 'admin': False, 'active': True, 'name': 'Kevin' },
        { 'admin': True, 'active': True, 'name': 'Bob' },
        { 'admin': True, 'active': False, 'name': 'John' },
        { 'admin': True, 'active': True, 'name': 'Keanu' }]

prefix = ""


for usr in user:
    if usr['admin'] and usr['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif usr['admin']:
        prefix = "(ADMIN) "
    elif usr['active']:
        prefix = "ACTIVE "

    print(prefix, usr['name'])


