"""
This module performs various calculations
between values
"""


def add_integer(a, b=98):
    """
    This function performs addition between
    two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
