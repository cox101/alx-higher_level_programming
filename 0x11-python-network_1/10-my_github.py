#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
   Uses the GitHub API to display your id"""

from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    credentials = HTTPBasicAuth(argv[1], argv[2])
    response = get("https://api.github.com/user", auth=credentials)
    print(response.json().get("id"))

