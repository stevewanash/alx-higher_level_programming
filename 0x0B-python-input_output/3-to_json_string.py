#!/usr/bin/python3
"""module uses json to do input and output
"""
import json


def to_json_string(my_obj):
    """represents an object in json format

    Args:
        my_obj (object): object to be encoded in json format

    Returns:
        str: json representation of object
    """
    return (json.dumps(my_obj))
