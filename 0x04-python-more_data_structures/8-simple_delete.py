#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    dic = a_dictionary.copy()
    if key in dic:
        del dic[key]
    return dic
