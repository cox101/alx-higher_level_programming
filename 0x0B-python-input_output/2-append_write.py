#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        - filename: Name of the text file to append (default is an empty string).
        - text: The string to append to the file (default is an empty string).

    Returns:
        int: Number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count

