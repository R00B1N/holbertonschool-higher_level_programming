#!/usr/bin/python3
"""
This module contains one function:
say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
        return
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
        return
    print("My name is {} {}".format(first_name, last_name))
