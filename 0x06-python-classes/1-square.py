#!/usr/bin/python3
"""Create a class square"""


class Square:
    """This class defines a square"""

    def __init__(self, size):
        """This function creates instances for the attribute size

        Args:
            size: size of the square's sides, without units

        """
        self.__size = size
