#!/usr/bin/python3
"""
module contains one class
"""


class Rectangle:
    """ class rectangle """
    def __init__(self, width=0, height=0):
        """ initiation """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """getter for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
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
        """ returns the rectangle's area """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangles's perimeter """
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ returns a printable string """
        wor = ""
        if self.__width == 0 or self.__height == 0:
            return wor
        for i in range(self.__height):
            for x in range(self.__width):
                wor += "#"
            wor += '\n'
        return wor[:-1]
