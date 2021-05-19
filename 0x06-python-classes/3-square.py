#!/usr/bin/python3
"""square"""


class Square:
    """what are these for? who knows"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """return the square's area"""
    def area(self):
        return self.__size * self.__size
