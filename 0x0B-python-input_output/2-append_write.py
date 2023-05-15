#!/usr/bin/python3
"""module handles input and output for files
"""


def append_write(filename="", text=""):
    """appends text to a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to be appended. Defaults to "".
    Returns:
        int: number of characters appended
    """
    with open(filename, 'a+', encoding='utf-8') as file:
        return (file.write(text))
