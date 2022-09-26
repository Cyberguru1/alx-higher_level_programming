#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix of integers
    """
    if matrix == [[]]:
        return
    x = len(matrix)
    for i in range(x):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]),end=' ')
            if j == len(matrix[i]):
                print('$')
        print('')
