#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer
    """

    def test_module_docstring(self):
        """Tests for module docstring"""

        mod_str = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod_str) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""

        func_docs = max_integer.__doc__
        self.assertTrue(len(func_docs) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""

        a = []
        self.assertIsNone(max_integer(a))

    def test_no_args(self):
        """Tests for no arguments passed to function"""

        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""

        b = [1]
        self.assertEqual(max_integer(b), 1)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""

        b = [99, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 99)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""

        m = [2, 10, 8, 120, 14, 50]
        self.assertEqual(max_integer(m), 120)

    def test_positive_end(self):
        """Tests for all positive with max at end"""

        e = [2, 10, 8, 36, 14, 80]
        self.assertEqual(max_integer(e), 80)

    def test_one_negative(self):
        """Tests for list with one negative number"""

        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""

        n = [-6, -50, -75, -1, -89]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """Tests for passing none as argument"""

        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""

        str = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(str)


if __name__ == "__main__":
    unittest.main()
