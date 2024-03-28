#!/usr/bin/python3
"""The script that fetches 'https://alx-intranet.hbtn.io/status' """

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data.decode('utf-8'))
