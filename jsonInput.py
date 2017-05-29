import requests
import json
from classes import Trains
from SqlCreate import addTrain

url = "https://api.rasp.yandex.net/v1.0/search/?apikey=723b350c-e13c-421b-a658-119b82b251a8&format=json&from= c10743&to=s2000006&lang=uk&date=2017-05-29&transport_types= suburban"
object = requests.get(url).text
try:
    dic = json.loads(object)
except json.decoder.JSONDecodeError:
    dic = {}

trainsList = []
if "threads" in dic:
    train = dic["threads"]
    for i in range(10):
        departure = ""
        arrival = ""
        fromTitle = ""
        toTitle = ""
        title = ""
        shortTitle = ""
        stops = ""
        if "departure" in train[i]:
            departure = train[i]["departure"]
        if "arrival" in train[i]:
            arrival = train[i]["arrival"]
        if "from" in train[i]:
            trainfrom = train[i]["from"]
            if "title" in trainfrom:
                fromTitle = trainfrom["title"]
        if "to" in train[i]:
            trainto = train[i]["to"]
            if "title" in trainto:
                toTitle = trainto["title"]
        if "thread" in train[i]:
            thread = train[i]["thread"]
            if "title" in thread:
                title = thread["title"]
            if "short_title" in thread:
                shortTitle = thread["short_title"]
        if "stops" in train[i]:
            stops = train[i]["stops"]
        tr = Trains(departure, arrival, fromTitle, toTitle, title, shortTitle, stops)
        addTrain(tr.departure, tr.arrival, tr.fromTitle, tr.toTitle, tr.title, tr.shortTitle, tr.stops)