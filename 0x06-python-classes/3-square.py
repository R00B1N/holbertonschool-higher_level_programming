#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0):
        if isinstance(size, int):
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
