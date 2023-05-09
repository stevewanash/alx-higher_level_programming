#!/usr/bin/python3
"""module creates a rectangle subclass
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """the constructor for class rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        """allows printing of output in a specific format

        Returns:
            str: describes the class and attributes
        """
        return "[{}] {}/{}".\
            format(self.__class__.__name__, self.__width, self.__height)

    def area(self):
        """calculates area

        Returns:
            int: product of width and height
        """
        return self.__width * self.__height
