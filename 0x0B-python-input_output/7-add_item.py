#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""

import sys
import json

def save_to_json_file(my_list, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_list, file)

if __name__ == "__main__":
    """Check if at least one argument is provided"""
    if len(sys.argv) < 2:
        print("Usage: {} arg1 arg2 ...".format(sys.argv[0]))
        sys.exit(1)
     """Extract command-line arguments"""
    arguments = sys.argv[1:]

    """ Load existing list or create a new one"""
    try:
        with open("add_item.json", mode='r', encoding='utf-8') as file:
            my_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        my_list = []

    """ Add arguments to the list"""
    my_list.extend(arguments)

    """Save the updated list to the file"""
    save_to_json_file(my_list, "add_item.json")

    print("Arguments added to add_item.json:", arguments)

