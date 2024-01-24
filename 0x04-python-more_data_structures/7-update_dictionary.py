#!/usr/bin/python3


"""Update dictionary."""
def update_dictionary(a_dictionary, key, value):
    """Fuction to make an update on dictionary."""
    new_dict = a_dictionary.copy()
    new_dict[key] = value
    return new_dict
