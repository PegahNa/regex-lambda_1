#####################################################
import re

# EXAMPLE 4 --- re.findall

"""
matches all of the regex patterns in the input string and returns a
list containing all the matched substrings. The only difference between
re.findall and re.finditer is that re.findall returns a list
instead of an iterator and contains matched substrings
instead of re.Match objects.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s\w+\s"
'''
In the regex above: match 'data' followed by a space char, 
followed by at least one alphanumeric char, followed by a space char'
'''

for matched in re.findall(regex, my_str):
    print(matched)


#####################################################