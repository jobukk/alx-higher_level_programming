#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""module Square"""


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
        - size: The size of the square.
        """
        super().__init__(size, size)  # Call superclass constructor with width and height as size
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Set size as a private attribute

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
