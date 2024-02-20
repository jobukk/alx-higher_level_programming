#!/usr/bin/python3
"""
Module with class MyList
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Method that sort a list"""
        filtered_list = [x for x in self if x is not None]
        sorted_list = sorted(list(filtered_list))
        print(sorted_list)
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)        

        