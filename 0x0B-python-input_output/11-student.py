#!/usr/bin/python3
"""uses json for input and output
"""


class Student:
    """student class
    """
    def __init__(self, first_name, last_name, age):
        """initialises student attributes

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictonary representation of instance

        Args:
            obj (class): instance of a class

        Returns:
            dict: dictionary representation of the
            instance
        """
        if attrs:
            return {key: self.__dict__[key] for key in self.__dict__ if key in
                    attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces attribute values of an instance with
        values of json object

        Args:
            json (dict): dictionary public attribute
            values
        """
        for key in self.__dict__:
            if key in json:
                self.__dict__[key] = json[key]
