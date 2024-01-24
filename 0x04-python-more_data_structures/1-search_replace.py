#!/usr/bin/python3
"""Search for a value and replace."""
def search_replace(my_list, search, replace):
    """Get the element then replace."""
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
