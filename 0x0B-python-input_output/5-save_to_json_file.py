#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: Python object to be serialized.
        filename (str): Name of the file to save the JSON representation.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
