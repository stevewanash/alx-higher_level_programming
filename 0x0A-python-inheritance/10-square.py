#!/usr/bin/python3
"""module inherits from class rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inheriting from rectangle
    """
    def __init__(self, size):
        """square class constructor

        Args:
            size (int): side dimensions of square
        """
        super().__init__(size, size)
        super().area()
