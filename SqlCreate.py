import sqlite
a = sqlite.db()
#a.query("CREATE TABLE Actors(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name INTEGER NOT NULL,"
#        " href TEXT NOT NULL, film TEXT NOT NULL);")

def (name, href, film):
    a.query("INSERT INTO Actors(name, href, film) values (\'%s\', \'%s\', \'%s\');" %(name, href, film))
    a.save()