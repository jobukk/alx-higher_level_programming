#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Use list comprehension and map
    to square each element in the matrix.
    """
    return [list(map(lambda x: x**2, row)) for row in matrix]
