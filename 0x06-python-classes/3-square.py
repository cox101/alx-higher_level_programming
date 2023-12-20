#!/usr/bin/python3

class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Instantiation with optional size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public method to calculate the area of the square."""
        return self.__size ** 2

