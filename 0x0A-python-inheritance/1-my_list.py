#!/usr/bin/python3
"""module creates a class that inherits from list
"""


class MyList(list):
    """a class that inherits from list
    """
    def print_sorted(self):
        """prints out a sorted list
        """
        print(sorted(self))
