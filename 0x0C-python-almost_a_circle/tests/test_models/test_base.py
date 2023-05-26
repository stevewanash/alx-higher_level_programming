#!/usr/bin/python3
"""unittests for the base class
"""
import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """tests the base class"""
    def test_to_json_string(self):
        """tests if object is converted to json string
        """
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1, "width": 8, "height": 4}]), '[{"id": 1, "width": 8, "height": 4}]')

    def test_from_json_string(self):
        """tests if json string is converted to object
        """
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1, "width": 8, "height": 4}]'), [{"id": 1, "width": 8, "height": 4}])
