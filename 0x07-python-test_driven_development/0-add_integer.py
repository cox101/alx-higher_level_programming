#!/usr/bin/python3
"""
Module add_integer
Define a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b,
    and raise an error if a and b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)

