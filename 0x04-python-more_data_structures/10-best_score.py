#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Function to get the highest score
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    score = 0
    k = ""
    for key in a_dictionary:
        if a_dictionary[key] > score:
            score = a_dictionary[key]
            k = key
    return k
