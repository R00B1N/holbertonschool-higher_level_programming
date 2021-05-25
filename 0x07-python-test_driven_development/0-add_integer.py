#!/usr/bin/python3
"""
This module contains one function:
add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    add_integer function returns the sum of 2 integers: a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
        return
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
        return
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
