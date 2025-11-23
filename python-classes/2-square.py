#!/usr/bin/python3
"""
Square class module.
"""


class Square:
    """Square with validated size."""

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size: Square size (default 0).

        Raises:
            TypeError: If size is not int.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square area."""
        return self.__size * self.__size
