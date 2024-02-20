#!/usr/bin/python3
"""Python script that for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{link}/users/{sys.argv[1]}").json()
    todos = requests.get(f"{link}/user/{sys.argv[1]}/todos").json()

    allcompleted = [t.get("title") for t in todos if t.get("completed")]
    print(f"Employee {user.get('name')} is \
done with tasks({len(allcompleted)}/{len(todos)}):")
    [print(f"\t {d}") for d in allcompleted]
