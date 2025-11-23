#!/usr/bin/python3
"""Module that defines a Square class with getter and setter for size."""


class Square:
    """Class that defines a square by its size and provides area computation."""

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size: The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value: The new size to assign.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size
