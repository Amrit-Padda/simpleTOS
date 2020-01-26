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
    for key in summarizedConcepts.keys():
        print(key)
