#!/usr/bin/env python3
"""
interview 7
"""


def rotate_2d_matrix(matrix):
    """
    interview roteted
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
