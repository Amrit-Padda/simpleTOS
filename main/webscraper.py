from bs4 import BeautifulSoup
import requests

def scrape_data_CGI(url):
    CGI_URL = url
    CGI_HTML = requests.get(CGI_URL).text
    CGI_SOUP = BeautifulSoup(CGI_HTML, 'html.parser')
    CGI_TEXT = CGI_SOUP.findAll("p", {"class": "align_left"}, text=True)
    paragraphs = []
    for x in CGI_TEXT:
        paragraphs.append(str(x))
    return paragraphs

def scrape_data_SHUTTERSTOCK(url):
    ST_URL = url
    ST_HTML = requests.get(ST_URL, headers={"User-Agent": "XY"}).text
    ST_SOUP = BeautifulSoup(ST_HTML, 'html.parser')
    ST_TEXT = ST_SOUP.findAll(['ol', 'b'])
    paragraphs = []
    for x in ST_TEXT:
        paragraphs.append(str(x))
    return paragraphs