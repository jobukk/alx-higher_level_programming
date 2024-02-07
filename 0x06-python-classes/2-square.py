#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Class that defines properties of square by:.

    Attributes:
        size: size of a square.
    """
    def __init__(self, size=0):
        """new instances of square.

        Args:
            size: size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
