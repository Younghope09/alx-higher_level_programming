#!/usr/bin/python3
"""Unittests for max_integer """

import unittest
max_integer = __import__('6-max_integer').max_integer
"""First, Import module and function"""

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered_list(self):
        """Testing ordered list of integers"""
        ordered_list = [3, 7, 9, 76]
        self.assertEqual(max_integer(ordered_list), 76)

    def test_unordered_list(self):
        """Testing unordered list of integers"""
        unordered_list = [3, 98, 54, 100]
        self.assertEqual(max_integer(unordered_list), 100)

    def test_maximum_at_begginning(self):
        """Testing list beginning with the maximum value"""
        maximum_integer_at_beginning = [54, 36, 21, 9]
        self.assertEqual(max_integer(maximum_integer_at_beginning), 54)

    def test_negative_list(self):
            """Testing list of negative"""
            negative_list = [-54, -36, -21, -9]
            self.assertEqual(max_integer(negative_list), -9)

    def test_empty_list(self):
        """Testing an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Testing list with a single element"""
        one_element_list = [4]
        self.assertEqual(max_integer(one_element_list), 4)
        
    def test_float(self):
        """Testing list of float"""
        float = [8.98]
        self.assertEqual(max_integer(float), 8.98)

    def test_floats(self):
        """Testing list of floats"""
        floats = [2.54, 6.23, 7.59, 5.09, 10.91]
        self.assertEqual(max_integer(floats), 10.91)

    def test_ints_and_floats(self):
        """Testing list of integers and floats"""
        integers_and_floats = [12.75, 15, -9.53, 86, 0.9]
        self.assertEqual(max_integer(integers_and_floats), 15)

    def test_string(self):
        """Test a string."""
        string = "twitter"
        self.assertEqual(max_integer(string), 'w')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["twitter", "is", "a", "place", "of", "violence"]
        self.assertEqual(max_integer(strings), "violence")

    def test_empty_string(self):
        """Test an empty string."""
        empty_string = ""
        self.assertEqual(max_integer(empty_string), None)

if __name__ == '__main__':
    unittest.main()
