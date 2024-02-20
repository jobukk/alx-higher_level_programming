#!/usr/bin/python3
"""
module with class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If the value is not an integer,
         raises a TypeError exception with the message
          "<name> must be an integer".
        - If the value is less than or equal to 0,
         raises a ValueError exception with the message
          "<name> must be greater than 0".

        Args:
        - name: A string representing the name of the value being validated.
        - value: The value to be validated.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
