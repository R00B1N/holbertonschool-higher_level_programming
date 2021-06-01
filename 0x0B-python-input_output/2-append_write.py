#!/usr/bin/python3
"""
This module contains one function
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a') as f:
        ap = f.write(text)
    return ap
