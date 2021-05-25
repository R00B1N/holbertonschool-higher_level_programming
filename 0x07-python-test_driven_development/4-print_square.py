#!/usr/bin/python3
"""
This module contains one function:
print_square(size)
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
        return
    if size < 0:
        raise ValueError('size must be >= 0')
        return
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
