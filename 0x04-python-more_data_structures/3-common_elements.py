#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    Function to output common elements.
    """
    array = []
    for i in set_1:
        for j in set_2:
            if i == j:
                array.append(i)
    return array
