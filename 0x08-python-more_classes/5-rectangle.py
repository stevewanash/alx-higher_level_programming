#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """this class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Function instantiates attributes

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        instance method for the string function

        Returns:
            string that can be printed by print()
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            picture = [
                '#' if j != self.__width else '' if j == self.__width and
                i == self.__height - 1 else '\n' for i in range(self.__height)
                for j in range(self.__width + 1)]
            return ("".join(picture))

    def __repr__(self):
        """
        is the method called by the repr function

        Returns:
            a value that can be evaluated using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        is the method called when an instance is deleted
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        sets the value for the width attribute

        Returns: instance value for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        is a setter function for the rectangle width

        Args:
            value: the width value

        Raises:
            Type error: when width is not an integer
            Value error: when width is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        sets the value for the height attribute

        Returns: instance value for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        is a setter function for the rectangle height

        Args:
            value: the height value

        Raises:
            Type error: when height is not an integer
            Value error: when height is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns area of the rectangle

        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter of the rectangle

        Returns:
            area of the rectangle
        """
        if self.__width != 0 and self.__height != 0:
            return 2*(self.__width + self.__height)
        else:
            return 0
