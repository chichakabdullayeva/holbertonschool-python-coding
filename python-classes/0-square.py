#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """Initializes the square with a given size.

        Args:
            size: The size of the square (no validation yet).
        """
        self.__size = size
