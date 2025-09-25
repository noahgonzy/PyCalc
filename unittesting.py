#unit testing for calculator.py
import calculator
import unittest

class TestCalculator(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculator.calculate("3+5"), "8.0")

if __name__ == '__main__':
    unittest.main()