from bs4 import BeautifulSoup
import requests
from classes import
from SqlCreate import

url = ""
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html5lib")
