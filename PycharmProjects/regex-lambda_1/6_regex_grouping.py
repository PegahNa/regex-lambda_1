#####################################################
import re

# EXAMPLE 6 --- GROUPING

"""
Sometimes we might want to match a regex pattern but only capture a
portion (or group) of it. Regex provides a simple way of doing this
by using the parenthesis (). We can define the group we want to capture
by surrounding it with () within the regex pattern.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s(\w+)\s"
'''
Match the word after 'data'
'''
for matched in re.findall(regex, my_str):
    print(matched)

#####################################################