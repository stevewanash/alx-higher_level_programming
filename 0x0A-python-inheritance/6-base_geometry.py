#!/usr/bin/python3
"""creating a class
"""


class BaseGeometry:
    """raises an exception
    """
    def area(self):
        """raises base class exception

        Raises:
            Exception: general exception
        """
        raise Exception("area() is not implemented")
