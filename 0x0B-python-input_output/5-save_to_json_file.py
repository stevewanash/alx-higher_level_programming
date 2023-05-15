#!/usr/bin/python3
"""module uses json to do input and output
"""
import json


def save_to_json_file(my_obj, filename):
    """decodes a json string to an object

    Args:
        my_str (str): string to be decoded from json format
        to object

    Returns:
        obj: object gotten from json string
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        json.dump(my_obj, file)
