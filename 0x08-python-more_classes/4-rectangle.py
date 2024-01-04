#!/usr/bin/python3
"""Module 4-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        return '\n'.join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value (int): value of the width, must be a positive integer
        """
        self._validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value (int): value of the height, must be a positive integer
        """
        self._validate_positive_integer("height", value)
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance"""
        return 2 * (self.__width + self.__height) if self.__height != 0 and self.__width != 0 else 0

    def _validate_positive_integer(self, attribute, value):
        """Validates if a value is a positive integer for width and height attributes."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

