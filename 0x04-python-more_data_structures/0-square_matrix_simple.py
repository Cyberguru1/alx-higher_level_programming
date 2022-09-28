#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    This function computes the square
    of all integers of a matrix
    """ 
    new_matrix = matrix.copy()
    for j in range(len(matrix)):
            new_matrix[j] = list(map(lambda x : x**2, matrix[j]))
    return new_matrix
