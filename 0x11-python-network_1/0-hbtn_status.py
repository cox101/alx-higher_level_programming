#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        data = response.read()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", data.decode(encoding='utf-8'))

