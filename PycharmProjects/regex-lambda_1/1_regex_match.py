#################################################
import re

# EXAMPLE 1 --- re.match

"""
matches the regex pattern starting from the beginning of the sentence 
and returns the matched substring. 
If something is found, then it returns a re.Match object; 
if not, it returns None
"""

my_str = "Nano Degree is fun"
regex = "Nano\s\w+\s"
'''
In the regex above: match 'Nano' followed by a space char, 
followed by at least one alphanumeric char, followed by a space char'
'''


matched = re.match(regex, my_str)
print(matched)

# To get the position of the matched substring and the text,
# we can use .span() and .group() , respectively.

print(matched.span())
print(matched.group())

#####################################################
