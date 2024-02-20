#!/usr/bin/python3
"""
module with class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Method for init the attributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to redefine area method in the parent class"""

        return self.__height * self.__width

    def __str__(self):
        """__str__ method for return the nxt string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
