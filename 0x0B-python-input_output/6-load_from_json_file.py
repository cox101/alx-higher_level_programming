#!/usr/bin/python3
"""Defines a JSON file-reading function."""

import json

def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        object: Python object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

