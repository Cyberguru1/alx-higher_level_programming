#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    This function computes the square
    of all integers of a matrix
    """
    sqr = lambda x : x**2
    new_matrix = matrix
    for i in (new_matrix):
        for j in (i):
            j = map(sqr, j)
    return new_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(square_matrix_simple(matrix))