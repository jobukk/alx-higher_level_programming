#!/usr/bin/python3
"""module Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
        - size: The size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        - The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the Square object.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
