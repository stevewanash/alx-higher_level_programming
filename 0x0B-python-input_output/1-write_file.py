#!/usr/bin/python3
"""module handles input and output for files
"""


def write_file(filename="", text=""):
    """overwrites text to a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to be written. Defaults to "".
    Returns:
        int: number of characters written to file
    """
    with open(filename, "w", encoding='utf-8') as file:
        return (file.write(text))
