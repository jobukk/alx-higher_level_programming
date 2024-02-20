#!/usr/bin/python3
"""Module Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for init the attributes"""

        super.__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area"""

        return self.__size * self.__size
