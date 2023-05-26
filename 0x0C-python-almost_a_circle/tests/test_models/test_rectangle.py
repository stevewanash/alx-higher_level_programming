#!/usr/bin/python3
"""unittests for the class rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests the class rectangle
    """
    def setUp(self):
        """sets up an instance for use in the tests
        """
        self.r1 = Rectangle(2, 2, 2, 2, 2)

    def tearDown(self):
        """tears down the set up instance"""
        del self.r1

    def test_area(self):
        """checks if area computing is accurate
        """
        self.assertEqual(self.r1.area(), 4)

    def test___init__(self):
        """checks if attribute initialization follows the rules
        """
        self.assertRaises(ValueError, Rectangle, 1, 0, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, "hi", 1, 1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -9, 1, 1, 1)

    def test___str__(self):
        """checks if instance returns correct format when print
        is called
        """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (2) 2/2 - 2/2")
