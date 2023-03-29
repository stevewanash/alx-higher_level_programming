#!/usr/bin/python3
"""Create a class square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This function creates instances for the attribute size

        Args:
            size: size of the square's sides, without units
            it is initialized to zero
        """
        self.__size = size

    def area(self):
        """
        Area function returns the area of the square

        Returns: Area of square
        """
        return self.__size**2

    @property
    def size(self):
        """
        Acts as a getter to retrieve size from attribute instance

        Returns: size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Acts as a setter to set size for an attribure instance

        Args:
            value (int): size of square's sides

        Raises:
            TypeError: if size type is not int

            ValueError: if size is less than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        prints out the square
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print('')
        else:
            print('')
