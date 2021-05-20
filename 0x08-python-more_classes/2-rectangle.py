#!/usr/bin/python3
"""
module contains one class
"""


class Rectangle:
    """ class Rectangle """
    def __init__(self, width=0, height=0):
        """ instantiation """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2
