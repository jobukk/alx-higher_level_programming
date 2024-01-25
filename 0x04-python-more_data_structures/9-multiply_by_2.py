#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Function to multiply dict values by a 2
    """
    dic = {}
    for k in a_dictionary:
        dic[k] = a_dictionary[k] * 2
    return dic
