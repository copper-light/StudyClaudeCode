import unittest
from calculator import multiply


class TestCalculator(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_float(self):
        self.assertEqual(multiply(2.5, 4), 10.0)


if __name__ == '__main__':
    unittest.main()
