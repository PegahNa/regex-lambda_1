#####################################################
import re

# EXAMPLE 2 --- re.search

"""
matches the regex pattern within the entire input sentence and returns
the first occurrence of the matched substring.
The difference between re.search and re.match is
that the matched substring of re.search does not have to start
from the beginning of the input string.
"""

my_str = "Software and Data Science 777 are fun"
regex = "Sci[\w\s]+\d+"
'''
In the regex above: match 'Sci' followed by a series of alphanumeric or space
char, followed by some digits
'''


matched = re.search(regex, my_str)
print(matched)

# To get the position of the matched substring and the text,
# we can use .span() and .group() , respectively.

print(matched.span())
print(matched.group())

#####################################################
