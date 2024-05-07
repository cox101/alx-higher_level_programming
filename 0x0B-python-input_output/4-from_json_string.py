#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
import json

import json

def from_json_string(my_str):
    """Returns the Python object represented by a JSON string.

    Args:
        my_str (str): JSON-formatted string.

    Returns:
        object: Python object represented by the JSON string.
    """
    return json.loads(my_str)

