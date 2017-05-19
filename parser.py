from bs4 import BeautifulSoup
import requests
from classes import Actors
import tablecreate

url = "https://www.kinopoisk.ru/film/522/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html5lib")

film = soup.find('h1', {'class': "moviename-big"}).text

actors = soup.findAll('li', {'itemprop': "actors"})
for actor in actors:
    name = actor.text
    ahref = actor.find('a')
    if ahref != None:
        href = ahref.get('href')
    else:
        href = None
    act = Actors(href, name, film)
    tablecreate.addActor(act.name, act.href, act.film)