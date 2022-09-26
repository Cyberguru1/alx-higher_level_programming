#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix of integers
    """
    if matrix == [[]]:
        return
    x = len(matrix)
    y = len(matrix[0][0])
    for i in range(x):
        for j in range(y):
            print("{:d}".format(matrix[i][j]),end=' ')
        print('')