#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for array in matrix:
        squares = map(lambda x : x**2, array)
        arr.append(list(squares))
    return arr
