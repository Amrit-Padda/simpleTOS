import os
import sys

def to_html(summarizedConcepts):
    f = open("output.html", mode="w+")
    f.write("<!DOCTYPE html>")
    f.write("<html>")
    f.write("<head>")
    f.write("<meta charset=\"utf-8\">")
    f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, shrink-to-fit=no\">")
    f.write("<title>Output</title>")
    f.write("</head>")
    f.write("<style>")
    f.write("body {background-color: #757474}")
    f.write("</style>")
    f.write("<body>")
    for key in summarizedConcepts: #Iterates over keys
        f.write("<h1 style=\"color:white\">" + key + "</h1>")
        f.write("<br>")
        f.write("<p1 style=\"color:white\">" + summarizedConcepts.get(key) + "</p1>")
        f.write("<br>")
    f.write("</body>")
    f.write("</html>")
    f.close()
    print("Outputted to File!")



