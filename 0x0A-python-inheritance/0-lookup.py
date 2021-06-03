#!/usr/bin/python3
"""
This module contains one function: lookup
"""


def lookup(obj):
    """
    function lookup(obj):
    returns a list of available attributes and methods of an object
    """
    return dir(obj)
