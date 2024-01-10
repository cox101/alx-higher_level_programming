/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys
from os.path import exists

def save_to_json_file(my_obj, filename):
    """Saves an object to a JSON file.

    Args:
        my_obj: Python object to be saved.
        filename (str): Name of the JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        object: Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "add_item.json"

    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)

