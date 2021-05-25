#!/usr/bin/python3
"""
This module contains one function:
matrix_divided(matrix, div) -> returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix (rounded to 2 decimal places)
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list or matrix == [[]]:
        raise TypeError(msg1)
        return
    for i in matrix:
        if type(i) is not list:
            raise TypeError(msg1)
            return
    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(msg1)
                return
    size = len(matrix[0])
    for i in matrix:
        if len(i) is not size:
            raise TypeError(msg2)
            return
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
        return
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return
    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(round((j / div), 2))
        new_matrix.append(row)
    return new_matrix
