#!/usr/bin/python3
"""
Square class module.
"""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialize square size."""
        self.size = size

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute area."""
        return self.__size * self.__size
