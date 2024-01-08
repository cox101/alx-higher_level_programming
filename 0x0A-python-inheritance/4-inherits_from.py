#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def is_inherited_from_class(obj, a_class):
    """Check if the object is an instance of a class inherited (directly or indirectly) from the specified class."""
    return issubclass(type(obj), a_class)
