import sys
import os

from ibmRequestHandler import *
from summarizationRequestHandler import *
"""
Important functions:
IBM:
parse_concepts("text") -- Replace text with the piece of text that you want to get the concepts for

Summary:
generate_summary(file_name, n) -- Generates summary of the given file and returns the top n lines(min: 1)
"""

os.chdir(os.getcwd() + "/TOS-Examples")
conceptList = parse_concepts("Dummy.txt")
print(conceptList)