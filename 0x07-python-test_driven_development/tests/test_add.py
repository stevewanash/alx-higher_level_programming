import unittest
s = __import__('0-add_integer')

class test_module(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(s.add_integer(2), 100)
        self.assertEqual(s.add_integer(2.000), 100)
        self.assertRaises(TypeError, s.add_integer, "Free")
        self.assertRaises(TypeError, s.add_integer, False)
        self.assertRaises(TypeError, s.add_integer, [1])
