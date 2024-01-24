#!/usr/bin/python3
"""Search for a value and replace."""
def search_replace(my_list, search, replace):
    """Get the element then replace."""
    new_list = my_list[:]
    for x in range(0,len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return new_list
