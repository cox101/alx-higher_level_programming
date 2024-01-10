#!/usr/bin/python3
""" function that inserts a line of text to a file"""

def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string after
    the search_string in filename.
    Args:
        - filename: name of the file
        - search_string: string to append after
        - new_string: new_string to append
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
