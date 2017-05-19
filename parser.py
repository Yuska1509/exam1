from bs4 import BeautifulSoup
import requests
from sqlite import DB

url = "https://www.kinopoisk.ru/film/522/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html5lib")

print(soup)