#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """safe printing function"""
    try:
        printed = 0
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
        print()
        return printed
    except IndexError:
        printed = 0
        for item in my_list:
            print(item, end="")
            printed += 1
        print()
        return printed
