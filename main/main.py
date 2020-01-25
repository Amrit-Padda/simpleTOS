import sys
import os
import tkinter #pip install tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

#Import our request handlers
sys.path.append(os.getcwd() + "/requestHandlers/")

import ibmRequestHandler as ibm
import summarizationRequestHandler as summarization
"""
Important functions:
IBM:
parse_concepts("text") -- Replace text with the piece of text that you want to get the concepts for

Summary:
generate_summary(file_name, n) -- Generates summary of the given file and returns the top n lines(min: 1)
"""

os.chdir(os.getcwd() + "/TOS-Examples")
summarization.generate_summary("Dummy.txt", 1)