#!/usr/bin/python3
"""
This module contains one class: Base
"""
import json
import csv


class Base:
    """
    The goal of this class is:
    to manage id attribute in all our future classes
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        l = []
        if list_objs is not None:
            for i in list_objs:
                l.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            m = cls(5)
        elif cls.__name__ == "Rectangle":
            m = cls(5, 5)
        m.update(**dictionary)
        return m

    @classmethod
    def load_from_file(cls):
        """
        reads a file and returns the list of instances
        that exist in the file
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                ls = cls.from_json_string(f.read())
                l = []
                for i in ls:
                    l.append(cls.create(**i))
                return l
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes attributes of list_objs to a csv file"""
        with open(cls.__name__ + ".csv", "w") as f:
            cwriter = csv.writer(f, delimiter=',')
            for obj in list_objs:
                my_l = []
                if cls.__name__ == "Rectangle":
                    my_l.append(obj.id)
                    my_l.append(obj.width)
                    my_l.append(obj.height)
                    my_l.append(obj.x)
                    my_l.append(obj.y)
                elif cls.__name__ == "Square":
                    my_l.append(obj.id)
                    my_l.append(obj.size)
                    my_l.append(obj.x)
                    my_l.append(obj.y)
                cwriter.writerow(my_l)

    @classmethod
    def load_from_file_csv(cls):
        """
        reads a csv file and returns the list of instances
        that exist in the file
        """
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                rs = csv.reader(f, delimiter=',')
                l = []
                if cls.__name__ == "Rectangle":
                    for i in rs:
                        r = cls(
                                int(i[1]),
                                int(i[2]),
                                int(i[3]),
                                int(i[4]),
                                int(i[0])
                                )
                        l.append(r)
                    return l
                elif cls.__name__ == "Square":
                    for i in rs:
                        r = cls(int(i[1]), int(i[2]), int(i[3]), int(i[0]))
                        l.append(r)
                    return l
        except:
            return []
