
import unittest

from addition import addition


class TestCalculator(unittest.TestCase):

    def test_addition_positive_numbers(self):
        self.assertEqual(addition(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(addition(-5, -3, "+"), -8)


if __name__ == "__main__":
    unittest.main()

