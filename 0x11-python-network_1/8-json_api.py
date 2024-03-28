#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        json_response = response.json()
        if json_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_response.get("id"), json_response.get("name")))
    except ValueError:
        print("Not a valid JSON")

