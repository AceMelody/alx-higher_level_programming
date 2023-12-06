#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row = []
    nmatrix = []
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            row.append(matrix[j][k] * matrix[j][k])
        nmatrix.append(row)
        row.clear()
    return nmatrix
