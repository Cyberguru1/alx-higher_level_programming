#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    This function computes the square
    of all integers of a matrix
    """
    sqr = lambda x : x**2
    new_matrix = [] 
    for j in matrix:
            new_matrix.append(list(map(sqr, j)))
    return new_matrix
