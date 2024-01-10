#!/usr/bin/python3
""" function that inserts a line of text to a file"""

def append_after(filename="", search_string="", new_string=""):
    """
    the search_string in filename.
    Args:
        - filename: name of the file
        - search_string: string to append after
        - new_string: new_string to append
    """

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string + '\n')

    except Exception as e:
        print(f"Error: {e}")
