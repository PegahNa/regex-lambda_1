#####################################################
import re

# EXAMPLE 7 --- COMPILING

"""
SO FAR, we have mainly used module-level functions provided by re directly.
Another way to perform regex pattern matching is to *compile* the pattern first
and then call the functions on the compiled object.

In general, we can use the compiled approach if we are going to use
the pattern MULTIPLE times; otherwise, it’s simpler to use the module-level
(non-compiled) functions.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s(\w+)\s"
pattern = re.compile(regex)
'''
Match the word after 'data'
'''
print("COMPILED EXAMPLE")
for matched in pattern.findall(my_str):
    print(matched)

#####################################################
