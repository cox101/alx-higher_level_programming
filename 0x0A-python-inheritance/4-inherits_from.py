#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def is_inherited_from_class(obj, a_class):
    """Check if the object is an instance of a class inherited (directly or indirectly) from the specified class."""
    """
    Checks if obj is an instance of a class inherited from a_class.
    
    Args:
        obj: The object to evaluate.
        a_class: The class to check against.
    
    Returns:
        True if obj is an instance of a class inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
