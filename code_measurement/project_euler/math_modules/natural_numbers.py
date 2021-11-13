import numpy as np


DIVISOR_FIVE = 5
DIVISOR_THREE = 3
DIVISOR_SEVEN = 7
DIVISOR_MINUS_FIVE = -5
DIVISOR_MINUS_THREE = -3
DIVISOR_MINUS_SEVEN = -7

divisors_list = [DIVISOR_FIVE, DIVISOR_THREE, DIVISOR_SEVEN, DIVISOR_MINUS_FIVE, DIVISOR_MINUS_THREE, DIVISOR_MINUS_SEVEN]

def get_natural_numbers_sum(lower_limit, divisors_list, upper_limit):
    # return sum(
    #     number
    #     for number in range(UPPER_LIMIT)
    #     if not number % DIVISOR_THREE or not number % DIVISOR_FIVE
    # )

    #divisors_list = []

    # while 1:
    #   for i in range(0,upper_limit):
    #     divisor = int(input('Enter a divisor less than {}'.format(upper_limit)))
    #     if divisor > upper_limit:
    #       print('You entered a divisor greater than upper limit, please enter a divisor less than upper limit')
    #       break
    #     elif divisors_list.count(divisor) >= 1:
    #       print('You cannot enter the same divisor twice')
    #       continue
    #     else:
    #       divisors_list.append(divisor)
    #       continue
    #   break
    
    '''Simuliranje korisničkog unosa funkcijom numpy.random.randint'''

    #divisors_set = set(np.random.randint(low=1,high=upper_limit,size=upper_limit - 1))

    natural_numbers_generator = (
      number
      for number in range(lower_limit + 1, upper_limit) #budući da se ne uzima upper_limit, ne uzima se ni lower_limit
      if [True if i % divisor_number == 0 else False for divisor_number in divisors_list].count(True) == len(divisors_list)
      #if sum(map((lambda x: number % x),divisors_set))
    )

    return np.sum(np.fromiter(natural_numbers_generator, int))
