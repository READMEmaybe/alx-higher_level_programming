#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""
    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test when the list contains a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test when the list contains positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        """Test when the list contains negative integers."""
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """Test when the list contains mixed positive and negative integers."""
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_duplicate_max(self):
        """Test when the list contains duplicate maximum values."""
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["These", "are", "strings"]), "strings")


if __name__ == '__main__':
    unittest.main()
