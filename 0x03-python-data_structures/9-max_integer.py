#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0] if my_list else None
    for i in my_list:
        if i > large:
            large = i
    return large
