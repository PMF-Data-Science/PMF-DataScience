import numpy


DIVISOR_FIVE = 5
DIVISOR_THREE = 3


def get_natural_numbers_sum(upper_limit):
    # return sum(
    #     number
    #     for number in range(UPPER_LIMIT)
    #     if not number % DIVISOR_THREE or not number % DIVISOR_FIVE
    # )

    natural_numbers_generator = (
      number
      for number in range(upper_limit)
      if not number % DIVISOR_THREE or not number % DIVISOR_FIVE
    )

    return numpy.sum(numpy.fromiter(natural_numbers_generator, int))
