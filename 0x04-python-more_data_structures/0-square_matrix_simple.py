#!/usr/bin/python3
"""Square element in matrix list."""
def square_matrix_simple(matrix=[]):
    """Loop through a matrix and utilize the map() to sqaure each elemt in matrix."""
    arr = []
    for array in matrix:
        squares = map(lambda x : x**2, array)
        arr.append(list(squares))
    return arr
