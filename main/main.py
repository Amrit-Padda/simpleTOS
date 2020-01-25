import sys
import os

#Import our request handlers
sys.path.append(os.getcwd() + "/simpleTOS/requestHandlers/")

from ibmRequestHandler import *
from summarizationRequestHandler import *
"""
Important functions:
IBM:
parse_concepts("text") -- Replace text with the piece of text that you want to get the concepts for

Summary:W
generate_summary(file_name, n) -- Generates summary of the given file and returns the top n lines(min: 1)
"""

adobe_TOS = "../TOS-Examples/Adobe-Legal-Terms.txt"

# generate_summary(adobe_TOS, 2)