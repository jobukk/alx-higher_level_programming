#!usr/bin/python3
"""
module with method inherits_from
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Args:
    - obj: The object to check.
    - a_class: The class to check against.

    Returns:
    - True if the object is an instance of a subclass of a_class,
    False otherwise.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
