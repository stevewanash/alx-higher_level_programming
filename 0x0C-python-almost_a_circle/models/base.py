#!/usr/bin/python3
"""creating base class with id
"""
import json


class Base:
    """base class with id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes id attribute

        Args:
            id (int, optional): id for each instance. Defaults to None.
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """converts object to json string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json representation of instance dictionaries
        to a json file"""
        filename = cls.__name__ + ".json"
        lis = []
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs:
                for i in range(len(list_objs)):
                    list_objs[i] = list_objs[i].__dict__
                json.dump(list_objs, file)
            else:
                json.dump(lis, file)

    def from_json_string(json_string):
        """converts json string to object"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """creates an instance out of a dictionary"""
        r = cls(1, 1, 1, 1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """convertes json string to list of dictionaries and
        converts the dictionaries to instances"""
        filename = cls.__name__ + ".json"
        with open(filename, 'r', encoding='utf-8') as file:
            c = 0
            dict_list = cls.from_json_string(file.read())
            for i in dict_list:
                dict_list[c] = cls.create(**i)
                c += 1
            return dict_list
