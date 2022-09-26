#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix of integers
    """
    if matrix == [[]]:
        return
    for i in range(len(matrix)):
        print("{:d} {:d} {:d}$".format(*matrix[i]))
