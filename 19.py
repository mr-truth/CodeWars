"""
Write a function that accepts a square matrix (N x N 2D array)
and returns the determinant of the matrix.
"""


def det(matrix, i, j):
    return [row[:j]+row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    sum_of_det = 0
    for col in range(len(matrix)):
        sign = (-1) ** col
        sub_det = determinant(det(matrix, 0, col))
        sum_of_det += (sign * matrix[0][col] * sub_det)
    return sum_of_det


matrix_NN = [[2, 4, 2],
             [3, 1, 1],
             [1, 2, 0]]
print(determinant(matrix_NN))