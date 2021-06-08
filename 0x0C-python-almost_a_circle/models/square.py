#!/usr/bin/python3
"""
This module containes the class Square, that inherits from the class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a Square is a special Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the string representation of an object """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the attributes of square """
        if args != ():
            if len(args) >= 2:
                newargs = args[0:2] + args[1:]
            else:
                newargs = args
            super().update(*newargs)
        else:
            newkwargs = dict()
            for k, v in kwargs.items():
                if k == "size":
                    newkwargs["width"] = v
                    newkwargs["height"] = v
                else:
                    newkwargs[k] = v
            super().update(**newkwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        ds = super().to_dictionary()
        ds["size"] = ds["height"]
        del ds["height"]
        del ds["width"]
        return ds
