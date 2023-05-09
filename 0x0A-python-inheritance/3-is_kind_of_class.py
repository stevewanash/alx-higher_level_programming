#!/usr/bin/python3
"""this module checks whether an object is part of
a class
"""


def is_kind_of_class(obj, a_class):
    """shows if an object is an instance of the
    specified class or its parent classes

    Args:
        obj: the object to be determined if instance
        a_class: the class to which the object
        is or isnt an instance
    Returns:
        True: if instance
        False: if not instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
