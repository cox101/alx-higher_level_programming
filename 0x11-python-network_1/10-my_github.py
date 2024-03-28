#!/usr/bin/python3
"""
Displays your GitHub id using GitHub API with Basic Authentication.
Usage: ./10-my_github.py <username> <personal_access_token>
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)

