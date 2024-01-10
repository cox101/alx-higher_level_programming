#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        - filename: Name of the text file to write (default is an empty string).
        - text: The string to write to the file (default is an empty string).

    Returns:
        int: Number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count

