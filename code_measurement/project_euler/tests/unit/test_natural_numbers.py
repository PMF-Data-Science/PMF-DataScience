import unittest
from random import randint, sample
from natural_numbers import get_natural_numbers_sum

class TestNaturalNumbersSum(unittest.TestCase):
    def test_sum_below_thousand(self):
        lower_limit = randint(-1000000, 1000000)
        upper_limit = randint(lower_limit, 1000001)
        all_divisors = [number for number in range(-20,20) if number != 0]
        divisors_length = randint(1, 10)
        divisors = sample(all_divisors, divisors_length)
        expected_result = sum(number for number in range(lower_limit+1,upper_limit) if any(not number % divisor for divisor in divisors ))
        self.assertEqual(get_natural_numbers_sum(lower_limit, divisors, upper_limit), expected_result)
