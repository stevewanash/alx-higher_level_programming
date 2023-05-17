"""uses json for input and output
"""


def class_to_json(obj):
    """returns json representation of instance
    dictionary containing attributes and their
    values

    Args:
        obj (class): instance of a class

    Returns:
        dict: json representation of the
        generated dictionary containing
        attributes and their values
    """
    return obj.__dict__
