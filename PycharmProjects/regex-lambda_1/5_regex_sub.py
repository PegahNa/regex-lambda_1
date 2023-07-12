#####################################################
import re

# EXAMPLE 5 --- re.sub

"""
matches all of the regex patterns in the input string
and substitutes them with the new_text provided.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s\w+\s"
'''
Substitute 'data science' and 'data analysis' with 'SQL queries'
'''
result = re.sub(regex, 'SQL queries ', my_str)
print(result)

#####################################################
