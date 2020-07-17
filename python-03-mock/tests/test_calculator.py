import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.calculator import Calculator
import unittest
from unittest import mock


def mock_sum(a, b):
    # mock sum function without the log running time.sleep(10)
    return a + b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator1 = Calculator()
        self.calculator2 = Calculator()
    def tearDown(self):
        self.calculator1 = None
        self.calculator2 = None
    # @mock.patch('lib.calculator.Calculator.sum', return_value=9) # hard coding return value
    # def test_sum(self, mock_sum):
    #     # result1 = self.calculator1.sum(2, 4)
    #     # result2 = self.calculator2.sum(-1, 1)
    #     self.assertEqual(mock_sum(2, 3), 9)
    #     # self.assertEqual(result2, 0)

    @mock.patch('lib.calculator.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(7, 2), 9)


if __name__ == "__main__":
    unittest.main()