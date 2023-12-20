#!/usr/bin/python3

class Square:
    """Class that defines a square with a private size attribute."""
    
    def __init__(self, size):
        """Instantiation with size (no type/value verification)."""
        self.__size = size

