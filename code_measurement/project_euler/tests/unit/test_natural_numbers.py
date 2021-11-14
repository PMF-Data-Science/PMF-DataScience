import unittest

from natural_numbers import get_natural_numbers_sum


class TestNaturalNumbersSum(unittest.TestCase):
    def test_sum_below_thousand(self, lower_limit, divisors, upper_limit):
        self.assertEqual(get_natural_numbers_sum(lower_limit, divisors, upper_limit), sum(number for number in range(lower_limit+1,upper_limit) if any(not number % divisor for divisor in divisors )))
