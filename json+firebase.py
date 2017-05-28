import requests
import json
from firebase import firebase
from classes import

url = ""
object = requests.get(url).text
dic = json.loads(object)

firebase_url = "https://exam-348bb.firebaseio.com/"
db = firebase.FirebaseApplication(firebase_url)

usersListOutout = []
if "response" in dic:
    list1 = dic["response"]
    if "users" in list1:
        listUsers = list1["users"]
        for user in listUsers:
            if "" in user:
                 = user[""]
            else:
                 = ""
            if "" in user:
                 = user[""]
            else:
                 = ""
            if "" in user:
                 = user[""]
            else:
                 = ""
            usersListOutout.append((, , ))

for user in usersListOutout:
    print(user.__dict__)
    db.post("/users", user.__dict__)

print(db.get("/users", None))