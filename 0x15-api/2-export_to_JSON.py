#!/usr/bin/python3
"""get infos"""
import json
import requests
import sys


if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{link}/users/{sys.argv[1]}").json()
    todos = requests.get(f"{link}/users/{sys.argv[1]}/todos").json()
    with open(f"{sys.argv[1]}.json", "w") as fout:
        json.dump({sys.argv[1]: [{"task": onetodo.get("title"),
                                  "completed": onetodo.get("completed"),
                                  "username": user.get('username')
                                  } for onetodo in todos]}, fout)
