#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if ((type(position) is not tuple) or (len(position) != 2)) \
            or (type(position[0]) is not int) \
            or (type(position[1]) is not int) \
                or ((position[0] < 0) or (position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((type(value) is not tuple) or (len(value) != 2)) \
            or (type(value[0]) is not int) \
            or (type(value[1]) is not int) \
                or ((value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
