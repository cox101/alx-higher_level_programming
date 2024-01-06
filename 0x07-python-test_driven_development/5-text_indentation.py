#!/usr/bin/python3
"""
Module text_indentation
Define a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of ., ? and :
    Args:
        text (str): Input text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev_char = ''
    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print()
        else:
            print(char, end='')
    print()

