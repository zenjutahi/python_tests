import unittest
from factorial import Factorial

class TddInFactorailExample(unittest.TestCase):

    def setUp(self):
        self.fact = Factorial()

    def test_factorial_returns_corrent_result(self):
        result = self.fact.recur_factorial(6)
        self.assertEqual(720, result)

    def test_factorial_returns_error_if_arg_not_a_number(self):
        self.assertRaises(ValueError, self.fact.recur_factorial, "six")


if __name__ == '__main__':
	unittest.main()