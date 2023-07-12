###############################################

#  Lambda Example with REDUCE
"""
Compare using REDUCE function without a lambda expression and then with it.

Reduce is another brilliant Python function.
It applies a ***rolling calculation to all items in a list***.
You could use this to tally up a sum total, or multiply all numbers together.
"""

# WITHOUT LAMBDA

from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]
print(numbers)


def sum_up(a, b):
    return a + b


result_A = reduce(sum_up, numbers)
print(result_A)

# WITH LAMBDA

result_B = reduce(lambda a, b: a + b, numbers)
print(result_B)

###############################################

alphabet = ['1', '2', '3']
print(reduce(lambda a, b: a + b, alphabet))