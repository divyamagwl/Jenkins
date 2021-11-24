#!/usr/bin/python3
# Test case for calculating multiplication of two numbers

import unittest
from program import multiply

class TestMean(unittest.TestCase):
    def test_mul1(self):
        result1 = multiply(12, 12)
        self.assertEqual(result1, 144)
    def test_mul2(self):
        result2 = multiply(10, 0)
        self.assertEqual(result2, 0)
    def test_mul3(self):
        result3 = multiply(10, 10)
        self.assertEqual(result3, 10)


if __name__ == '__main__':
    unittest.main()
