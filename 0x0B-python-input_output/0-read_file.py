#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): Name of the text file to read.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
