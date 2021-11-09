import unittest

from natural_numbers import get_natural_numbers_sum


class TestNaturalNumbersSum(unittest.TestCase):
    def test_sum_below_thousand(self):
        self.assertEqual(get_natural_numbers_sum(), 233168)
