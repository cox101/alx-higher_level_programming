#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    
    Args:
        - filename: Name of the text file to read (default is an empty string).
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")

