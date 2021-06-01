#!/usr/bin/python3
"""
This module contains one class
"""


class Student:
    """
    Public instance attributes:
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            d = dict()
            for i in attrs:
                if i in self.__dict__:
                    d[i] = self.__dict__[i]
            return d

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for k in json.keys():
            self.__dict__[k] = json[k]
