#!/usr/bin/python3
"""
This module contains one function
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w') as f:
        wr = f.write(text)
    return wr
