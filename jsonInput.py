import requests
import json
from classes import Trains
from SqlCreate import addTrain

url = "https://api.rasp.yandex.net/v1.0/search/?apikey=723b350c-e13c-421b-a658-119b82b251a8&format=json&from= c10743&to=s2000006&lang=uk&date=2017-05-29&transport_types= suburban"
#url = "https://sqliteonline.com/"
object = requests.get(url).text
#print(object)
#print(type(object))
dic = json.loads(object)


trainsList = []
if "threads" in dic:
    list1 = dic["threads"]
    for train in list1:
        departure = ""
        arrival = ""
        fromTitle = ""
        toTitle = ""
        title = ""
        shortTitle = ""
        stops = ""
        if "departure" in train:
            departure = train["departure"]
        if "arrival" in train:
            arrival = train["arrival"]
        if "from" in train:
            trainfrom = train["from"]
            if "title" in trainfrom:
                fromTitle = trainfrom["title"]
        if "to" in train:
            trainto = train["to"]
            if "title" in trainto:
                toTitle = trainto["title"]
        if "thread" in train:
            thread = train["thread"]
            if "title" in thread:
                title = thread["title"]
            if "short_title" in thread:
                shortTitle = thread["short_title"]
        if "stops" in train:
            stops = train["stops"]
        tr = Trains(departure, arrival, fromTitle, toTitle, title, shortTitle, stops)
        addTrain(tr.departure, tr.arrival, tr.fromTitle, tr.toTitle, tr.title, tr.shortTitle, tr.stops)