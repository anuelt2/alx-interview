#!/usr/bin/python3
"""Module for rotate_2d_matrix function"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise"""
    size = len(matrix)

    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
