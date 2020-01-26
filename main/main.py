import sys
import os

from ibmRequestHandler import *
from summarizationRequestHandler import *
from webscraper import *
"""
Important functions:
IBM:
parse_concepts("text") -- Replace text with the piece of text that you want to get the concepts for

Summary:
generate_summary(text, n) -- Generates summary of the given text and returns the top n lines(min: 1)
"""
url = 'https://www.cgi.com/en/legal-restrictions'

os.chdir(os.getcwd() + "/TOS-Examples")

conceptsSummarized = dict()
paragraphs = scrape_data(url)# Would return an array of all web-scraped paragraphs
for paragraph in paragraphs:
    conceptsSummarized.update({parse_concepts(paragraph)[0] : generate_summary(paragraph, 2)}) #Add the concept and a summary of it to the list

print(conceptsSummarized)