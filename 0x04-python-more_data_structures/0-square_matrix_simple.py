#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    f = lambda x : x**2
    for i in range(len(matrix)):
            new_matrix[i] = list(map(f, matrix[i]))

    return new_matrix
