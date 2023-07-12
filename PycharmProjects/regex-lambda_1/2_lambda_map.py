#  Lambda Example with MAP
# """
# Compare using MAP function without a lambda expression and then with it.
#
# Remember, the map function expects two arguments: a function and a list.
# It takes the transformation function and applies it
# to ***every element in the list***,
# returning the list of modified elements as a map object.
# This is why we use list() again to convert
# the resulting map object back into a list again.
# """
# # WITHOUT LAMBDA

my_list = [2, 4, 6, 8]
print(my_list)


def add_five(number):
    return number + 5


new_list_A = list(map(add_five, my_list))
print(new_list_A)

# WITH LAMBDA

new_list_B = list(map(lambda x: x + 5, my_list))
print(new_list_B)

# In this case we did not need to define a separate function like 'add_five',
# we just used lambda in a single expression.
