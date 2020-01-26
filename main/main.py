import sys
import os
import re
from ibmRequestHandler import *
from summarizationRequestHandler import *
from webscraper import *
from toHTML import *
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
paragraphs = scrape_data_SHUTTERSTOCK('https://www.shutterstock.com/terms')# Would return an array of all web-scraped paragraphs

for i in range(len(paragraphs)):
    replaced = re.sub("\<(.*?)\>", "", paragraphs[i])
    generate_summary(replaced, 1)
    #conceptsSummarized.update({parse_concepts(replaced)[0] : generate_summary(f2, 2)}) #Add the concept and a summary of it to the list

print(conceptsSummarized)