from bs4 import BeautifulSoup
import requests

CGI_URL = 'https://www.cgi.com/en/legal-restrictions'
CGI_HTML = requests.get(CGI_URL).text
CGI_SOUP = BeautifulSoup(CGI_HTML, 'html.parser')
CGI_TEXT = CGI_SOUP.findAll("p", {"class": "align_left"})

print(CGI_TEXT)