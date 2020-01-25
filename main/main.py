import sys
import os
import tkinter #pip install tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

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
os.chdir(os.getcwd() + "/simpleTOS/TOS-Examples")
generate_summary("Dummy.txt", 1)