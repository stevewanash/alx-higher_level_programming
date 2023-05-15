#!/usr/bin/python3
"""module uses json to do input and output
"""
import json


def from_json_string(my_str):
    """decodes a json string to an object

    Args:
        my_str (str): string to be decoded from json format
        to object

    Returns:
        obj: object gotten from json string
    """
    return (json.loads(my_str))
