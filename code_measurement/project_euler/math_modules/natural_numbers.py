import numpy as np

def get_natural_numbers_sum(lower_limit, divisors, upper_limit):

    '''Summation of numbers in the range of <lower_limit, upper_limit> that are divisible by at least one divisor from the list of divisors'''

    natural_numbers_generator = (
      number
      for number in range(lower_limit + 1, upper_limit) 
      if any(not number % divisor for divisor in divisors)
    )

    return np.sum(np.fromiter(natural_numbers_generator, int))
