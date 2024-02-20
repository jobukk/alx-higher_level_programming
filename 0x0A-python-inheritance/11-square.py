#!/usr/bin/python3
"""Module Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
        - size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
