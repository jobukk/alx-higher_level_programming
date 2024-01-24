#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return
    score = 0
    k = "" 
    for key in a_dictionary:
        if a_dictionary[key] > score:
            score = a_dictionary[key]
            k = key
    return k
