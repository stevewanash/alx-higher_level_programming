#!/usr/bin/python3
"""uses json for input and output
"""


def class_to_json(obj):
    """returns dictonary representation of instance

    Args:
        obj (class): instance of a class

    Returns:
        dict: dictionary representation of the
        instance
    """
    return obj.__dict__
