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
cgi_url = 'https://www.cgi.com/en/legal-restrictions'
st_tou_url = 'https://www.shutterstock.com/terms'
st_tos_url = 'https://www.shutterstock.com/license'

os.chdir(os.getcwd() + "/TOS-Examples")

conceptsSummarized = dict()
#paragraphs = scrape_data_SHUTTERSTOCK(st_tou_url)# Would return an array of all web-scraped paragraphs
paragraphs = scrape_data_CGI(cgi_url)
# -4 is a hardcoded value configured for CGI's ToS
for i in range(len(paragraphs) - 4):
    clean_paragraph = re.sub("\<(.*?)\>", "", paragraphs[i])
    clean_paragraph = re.sub(r'[^\x00-\x7F]+',' " ', clean_paragraph)
    # ignore one word lines
    if clean_paragraph.find(".") == -1:
        continue
    else:
        concept = parse_concepts(clean_paragraph)[0]

    summary = generate_summary(clean_paragraph, 1)

    # Avoids overriding concept data when appending new info to it
    if concept in conceptsSummarized:
        if conceptsSummarized[concept].endswith('.'): #If the last character is a period, then just add space after
            conceptsSummarized.update({concept : conceptsSummarized[concept] + " <br><br>" + (summary)})
        else:
            conceptsSummarized.update({concept : conceptsSummarized[concept] + ".<br><br>" + (summary)})
    else:
        conceptsSummarized.update({concept : summary}) #Add the concept and a summary of it to the list

to_html(conceptsSummarized)
