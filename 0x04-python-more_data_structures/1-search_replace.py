#!/usr/bin/python3
"""Search for a value and replace."""
def search_replace(my_list, search, replace):
    """Get the element then replace."""
    new_list = []
    for elem in range(0,len(my_list)):
        if my_list[elem] == search:
            new_list.append(replace)
        else:
            new_list.append(elem)
    return new_list
