#!/usr/bin/python3
"""get infos"""
import csv
import requests
import sys


if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{link}/users/{sys.argv[1]}").json()
    todos = requests.get(f"{link}/users/{sys.argv[1]}/todos").json()
    with open(f"{sys.argv[1]}.csv", mode="w") as fout:
        writer = csv.writer(fout, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([sys.argv[1], user.get("username"),
                             t.get("completed"), t.get("title")])
