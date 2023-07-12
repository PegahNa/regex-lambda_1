#####################################################
import re

# EXAMPLE 3 --- re.finditer

"""
matches all of the regex patterns in the input string and
returns an iterator containing all the re.Match
objects of the matched substrings.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s\w+\s"
'''
In the regex above: match 'data' followed by a space char, 
followed by at least one alphanumeric char, followed by a space char'
'''

for matched in re.finditer(regex, my_str):
    print(matched)


#####################################################