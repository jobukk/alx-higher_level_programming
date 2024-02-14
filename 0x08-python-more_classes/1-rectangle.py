#!/usr/bin/python3
"""1-rectangle
"""


class Rectangle:
    """The class only creates private instance attibutes by taking in two arguments.

    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0

    """    
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.__width = width
        self.__height = height
        

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """    
        return self.__width
    
    @width.setter
    def width(self, value):
        """Args:
            value (int): dimension of rectangle

        Attributes:
            __width (int): dimension of rectangle

        Raises:
            TypeError: If 'value' is not an int.
            ValueError: If 'value' is less than 0

        """            
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension

        """    
        return self.__height
    
    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension

        Attributes:
            __height (int): vertical dimension

        Raises:
            TypeError: If 'value' is not an int.
            ValueError: If 'value' is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
