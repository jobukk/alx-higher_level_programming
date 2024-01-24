#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    array = []
    for i in set_1:
        if i not in set_2:
           array.append(i)
    for i in set_2:
        if i not in set_1:
           array.append(i)       
            
    return array
