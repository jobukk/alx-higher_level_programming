#!/usr/bin/python3
"""Search for a value and replace."""
def search_replace(my_list, search, replace):
    """Get the element then replace."""
    new_list = my_list[:]
    the_index = new_list.index(search)
    new_list[the_index] = replace
    return new_list
