#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
module with class Rectangle
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with width and height.

        Args:
        - width: Width of the rectangle.
        - height: Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height