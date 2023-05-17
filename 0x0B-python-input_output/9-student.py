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

    def to_json(self):
        """returns dictonary representation of instance

        Args:
            obj (class): instance of a class

        Returns:
            dict: dictionary representation of the
            instance
        """
        return self.__dict__
