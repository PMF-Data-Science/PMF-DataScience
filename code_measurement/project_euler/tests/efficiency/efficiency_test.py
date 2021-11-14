from math_modules import natural_numbers
import timeit

measurements_dict = {}
UPPER_LIMIT1 = 10000
UPPER_LIMIT2 = 50000
UPPER_LIMIT3 = 70000
UPPER_LIMIT4 = 100000
UPPER_LIMIT5 = 500000
UPPER_LIMIT6 = 700000
UPPER_LIMIT7 = 1000000

LOWER_LIMIT1 = -10000
LOWER_LIMIT2 = -50000
LOWER_LIMIT3 = -70000
LOWER_LIMIT4 = -100000
LOWER_LIMIT5 = -500000
LOWER_LIMIT6 = -700000
LOWER_LIMIT7 = -1000000

upper_limits = [UPPER_LIMIT1, UPPER_LIMIT2, UPPER_LIMIT3, UPPER_LIMIT4, UPPER_LIMIT5, UPPER_LIMIT6, UPPER_LIMIT7]
lower_limits = [LOWER_LIMIT1,LOWER_LIMIT2,LOWER_LIMIT3,LOWER_LIMIT4,LOWER_LIMIT5,LOWER_LIMIT6,LOWER_LIMIT7]

limits = zip(upper_limits,lower_limits)

def test_efficiency(divisors):
        for limit in limits:
                measurements_dict.update({limit[1]:timeit.timeit(lambda:natural_numbers.get_natural_numbers_sum(limit[0], divisors, limit[1]), number=1)})
        return measurements_dict
\n
