#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('16-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 5, 9]), 9)
    def test_float(self):
        self.assertEqual(max_integer([1.8, 2.9, 0.3]), 2.9)
    def test_bool(self):
        self.assertEqual(max_integer([True, False]), True)
    def test_list(self):
        self.assertEqual(max_integer([[1,2], [3,4], [4,5]]), [4,5])
    def test_tuple(self):
        self.assertEqual(max_integer([(1,2), (3,4), (4,5)]), (4,5))
    def test_int_float(self):
        self.assertEqual(max_integer([5.6, 8, 2.4, 40]), 40)
    def test_int_bool(self):
        self.assertEqual(max_integer([True, 98, False, 402]), 402)
    def test_float_bool(self):
        self.assertEqual(max_integer([True, 0.8, False, 4.2]), 4.2)
    def test_reverse(self):
        self.assertEqual(max_integer([6, 3, 2, 0]), 6)
    def test_same(self):
        self.assertEqual(max_integer([12, 12, 12]), 12)
    def test_negative(self):
        self.assertEqual(max_integer([-21, -2, -13, -46]), -2)
    def test_big(self):
        self.assertEqual(max_integer([-49, -11, 892, 99999999999999999999999999999999999999]), 99999999999999999999999999999999999999)
    def test_char(self):
        self.assertEqual(max_integer('c'), 'c')
    def test_chars(self):
        self.assertEqual(max_integer(['a', 'b', 'c']),'c')
    def test_string(self):
        self.assertEqual(max_integer('string'), 't')
    def test_strings(self):
        self.assertEqual(max_integer(['bye', 'hi', 'z']),'z')
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    def test_none_list(self):
        with self.assertRaises(TypeError):
            max_integer([None, 2])
    def test_mix_list(self):
        with self.assertRaises(TypeError):
            max_integer(['z', 1.2, 2])
    def test_str_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([-27, 23, "hi"])

if __name__ == '__main__':
    unittest.main()
