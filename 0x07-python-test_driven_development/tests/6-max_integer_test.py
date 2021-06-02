#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testlist(unittest.TestCase):
    """
    This class contains tests for the function max_integer in 6-max_integer.py
    """
    def test_max(self):
        """ method that holds the tests
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([10, 2, 3]), 10)
        self.assertEqual(max_integer([1, 1, 0, -3]), 1)
        self.assertEqual(max_integer([5, 7, 9, 8, 9, 1]), 9)
        self.assertEqual(max_integer("helloez"), "z")
        self.assertEqual(max_integer([[5, 0], [4, 20]]), [5, 0])
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        with self.assertRaises(TypeError):
            max_integer(["hello", 1, 2])
