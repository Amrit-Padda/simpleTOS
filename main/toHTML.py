import os
import sys
"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Output</title>
</head>

<body>
    <>
</body>
</html>
"""

def to_html(summarizedConcepts):
    f = open("output.html", mode="w+")
    f.write("<!DOCTYPE html>")
    f.write("<html>")
    f.write("<head>")
    f.write("<meta charset=\"utf-8\">")
    f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, shrink-to-fit=no\">")
    f.write("<title>Output</title>")
    f.write("</head>")
    f.write("<body>")
    for key in summarizedConcepts.keys():
        if len(summarizedConcepts.get(key)) != 1: #1 Word aka what the header should be
            f.write("<h1>" + str(summarizedConcepts.get(key) + "</h1>"))
            f.write("<br>")
        else:
            f.write("<p1>" + str(summarizedConcepts.get(key)) + "</p1>")
            f.write("<br>")
    f.write("</body>")
    f.write("</html>")



