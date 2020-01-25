import sys
import os

#Import our request handlers
sys.path.append(os.getcwd() + "/simpleTOS/requestHandlers/")

from simpleTOS.code.ibmRequestHandler import * as ibm
from simpleTOS.requestHandlers.summarizationRequestHandler import * as summary

"""
Important functions:
IBM:
ibm.parse_concepts("text") -- Replace text with the piece of text that you want to get the concepts for

Summary:
summary.generate_summary(file_name, n) -- Generates summary of the given file and returns the top n lines(min: 1)
"""


