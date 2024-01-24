#!/usr/bin/python3


"""A function to delete."""
def simple_delete(a_dictionary, key=""):
    """Fuction to delete a key."""
    dic = a_dictionary.copy()
    if key in dic:
        del dic[key]
    return dic
