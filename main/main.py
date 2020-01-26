import sys
import os

from ibmRequestHandler import *
from summarizationRequestHandler import *
"""
Important functions:
IBM:
parse_concepts("text") -- Replace text with the piece of text that you want to get the concepts for

Summary:
generate_summary(text, n) -- Generates summary of the given text and returns the top n lines(min: 1)
"""
os.chdir(os.getcwd() + "/TOS-Examples")

#conceptsSummarized = dict()
#paragraphs = get_scraping_results() Would return an array of all web-scraped paragraphs
#for paragraph in paragraphs:
 #   concept = parse_concepts(paragraph) #Get the main concept of the paragraph
 #   conceptsSummarized.update({concept[0] : generate_summary(paragraph, 2)}) #Add the concept and a summary of it to the list
##Lambda expression to check for double new line

print(conceptsSummarized)