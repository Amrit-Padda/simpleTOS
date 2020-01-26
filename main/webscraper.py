from bs4 import BeautifulSoup
import requests

def scrape_data(url):
    CGI_URL = url
    CGI_HTML = requests.get(CGI_URL).text
    CGI_SOUP = BeautifulSoup(CGI_HTML, 'html.parser')
    CGI_TEXT = CGI_SOUP.findAll("p", {"class": "align_left"})

    return CGI_TEXT