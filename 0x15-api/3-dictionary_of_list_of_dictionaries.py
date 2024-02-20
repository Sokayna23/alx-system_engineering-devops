#!/usr/bin/python3
"""get infos"""
import json
import requests


if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{link}users").json()

    with open("todo_all_employees.json", "w") as fout:
        ar = {u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
                } for t in requests.get(f"{link}users\
                /{u.get('id')}/todos").json()] for u in users}
        json.dump(ar, fout)
