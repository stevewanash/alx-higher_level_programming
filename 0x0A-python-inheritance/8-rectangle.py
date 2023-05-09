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
