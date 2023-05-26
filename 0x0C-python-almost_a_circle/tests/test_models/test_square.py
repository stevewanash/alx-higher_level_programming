#!/usr/bin/python3
"""unittests for the class square"""
import unittest
from models.square import Square


class Test_square(unittest.TestCase):
    """tests the square class
    """
    def test___init__(self):
        """checks if initialization follows the given
        rules
        """
        self.assertRaises(ValueError, Square, 0, 1, 1, 1)
        self.assertRaises(TypeError, Square, "hi", 1, 1, 1)
        self.assertRaises(ValueError, Square, -9, 1, 1, 1)
