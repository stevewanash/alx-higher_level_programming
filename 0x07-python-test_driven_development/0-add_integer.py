"""
This module performs various calculations
between values
"""


def add_integer(a, b=98):
    """
    This function performs addition between
    two integers
    """
    try:
        if type(a) not in [int, float]:
            raise TypeError
    except TypeError:
        print("a must be an integer")
    try:
        if type(b) not in [int, float]:
            raise TypeError
    except TypeError:
        print("b must be an integer")
    try:
        return (int(a) + int(b))
    except TypeError:
        return
