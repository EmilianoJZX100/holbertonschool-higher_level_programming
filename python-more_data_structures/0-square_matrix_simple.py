#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for idx, j in (matrix[i]):
            matrix[i][j] = matrix[i][j] * matrix[i][j]
    return matrix

