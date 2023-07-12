###############################################

#  Lambda Example with FILTER
"""
Compare using FILTER function without a lambda expression and then with it.

Remember, with the filter function, the process is very similar.
Filter takes a function and applies it to every element in a list.
It creates a new list with
***only the elements that made the function to return True***.
"""
# WITHOUT LAMBDA

numbers = [1, 4, 5, 10, 20, 30]
print(numbers)


def greater_than_five(number):
    if number > 5:
        return True
    else:
        return False


new_numbers_A = list(filter(greater_than_five, numbers))
print(new_numbers_A)

# WITH LAMBDA

new_numbers_B = list(filter(lambda x: x > 5, numbers))
print(new_numbers_B)

# In this case we did not need to define a separate filter function
# like 'greater_than_five', we just used lambda in a single expression.

###############################################
