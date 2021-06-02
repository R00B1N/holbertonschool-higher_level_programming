#!/usr/bin/python3
"""
This module contains one fucntion
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    big = []
    big.append([1, ])
    for i in range(0, n - 1):
        small = [1, ]
        for j in range(0, len(big[-1]) - 1):
            small.append(big[-1][j] + big[-1][j + 1])
        small.append(1)
        big.append(small)
    return big
