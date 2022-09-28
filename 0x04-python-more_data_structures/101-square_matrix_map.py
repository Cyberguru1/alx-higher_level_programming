#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = [list(map(lambda x: x**2, matrix[i]) for i in range(len(matrix)))]
    return (new_matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)