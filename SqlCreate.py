import sqlite
a = sqlite.db()
#a.query("CREATE TABLE Trains(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, departure TEXT NOT NULL, arrival TEXT NOT NULL, fromTitle TEXT NOT NULL, toTitle TEXT NOT NULL, title TEXT NOT NULL, shortTitle TEXT NOT NULL, stops TEXT NOT NULL);")

def addTrain(departure, arrival, fromTitle, toTitle, title, shortTitle, stops):
    a.query("INSERT INTO Trains(departure, arrival, fromTitle, toTitle, title, shortTitle, stops) values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');" %(departure, arrival, fromTitle, toTitle, title, shortTitle, stops))
    a.save()