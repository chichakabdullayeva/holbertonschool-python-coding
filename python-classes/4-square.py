#!/usr/bin/python3
"""
Square class module.
"""


class Square:
    """Square with size, area and print."""

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

    def my_print(self):
        """Print square using '#'. """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
