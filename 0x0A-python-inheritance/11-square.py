#!/usr/bin/python3
"""
This module contains one class: Square, that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ contains __init__ method """
    def __init__(self, size):
        """
        instantiation
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
