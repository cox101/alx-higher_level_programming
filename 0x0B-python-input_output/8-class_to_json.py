#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""

def class_to_json(obj):
    """Converts an object to a serializable dictionary.

    Args:
        obj: Instance of a Class with serializable attributes.

    Returns:
        dict: Dictionary representation of the object.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
