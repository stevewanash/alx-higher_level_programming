#!/usr/bin/python3
"""creating a class
"""


class BaseGeometry:
    """raises exceptions
    """
    def area(self):
        """raises base class exception

        Raises:
            Exception: general exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises two exceptions

        Args:
            name (str): descriptor of the value
            value (int): value to be validated

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if not value > 0:
            raise ValueError("{} must be greater than 0".format(name))
