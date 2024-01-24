#!/usr/bin/python3


"""Add elements."""
def uniq_add(my_list=[]):
    """Fuction to add the elements in a list."""
    add = 0
    for i in set(my_list):
        add += i
    return add
