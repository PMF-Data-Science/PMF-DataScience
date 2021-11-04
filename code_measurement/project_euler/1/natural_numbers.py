import numpy


DIVISOR_THREE = 3
DIVISOR_FIVE = 5
UPPER_LIMIT = 1000


def get_natural_numbers_sum():
    # return sum(
    #     number
    #     for number in range(UPPER_LIMIT)
    #     if not number % DIVISOR_THREE or not number % DIVISOR_FIVE
    # )

    natural_numbers_generator = (
      number
      for number in range(UPPER_LIMIT)
      if not number % DIVISOR_THREE or not number % DIVISOR_FIVE
    )

    return numpy.sum(numpy.fromiter(natural_numbers_generator, int))
