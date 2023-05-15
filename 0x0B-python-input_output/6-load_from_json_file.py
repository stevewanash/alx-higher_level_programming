#!/usr/bin/python3
"""module uses json to do input and output
"""
import json


def load_from_json_file(filename):
    """creates object from json file

    Args:
        filename: name of JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (json.load(file))
