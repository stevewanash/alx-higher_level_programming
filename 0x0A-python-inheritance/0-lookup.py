#!/usr/bin/python3
"""
Creating a function with an object input
"""


def lookup(obj):
    """Function returns list of attributes and
     methods in obj

    Args:
        obj: class with attributes and methods within
        it.
    """
    return (dir(obj))
