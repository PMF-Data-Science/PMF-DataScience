import numpy as np

def get_natural_numbers_sum(lower_limit, divisors, upper_limit):

    '''Sumiranje brojeva u rasponu od (donja_granica, gornja_granica) koji su djeljivi s barem jednim djeliteljom iz liste divisors'''

    #divisors_set = set(np.random.randint(low=1,high=upper_limit,size=upper_limit - 1))

    natural_numbers_generator = (
      number
      for number in range(lower_limit + 1, upper_limit) #budući da se ne uzima upper_limit, ne uzima se ni lower_limit
      if any(not number % divisor for divisor in divisors)
      #if sum(map((lambda x: number % x),divisors_set))
    )

    return np.sum(np.fromiter(natural_numbers_generator, int))
