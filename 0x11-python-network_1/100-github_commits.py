#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")

