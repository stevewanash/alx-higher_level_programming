#!/usr/bin/python3
"""module handles input and output for files
"""


def read_file(filename=""):
    """reads a file and prints to STDOUT

    Args:
        filename (str, optional): file name as a path. Defaults to "".
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
