import requests
import json
from firebase import firebase
from classes import Users

#url = "https://api.vk.com/method/database.getSchools?city_id=1"
url = "https://api.vk.com/method/groups.getMembers?group_id=33393308&fields=city,nickname"
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
            if "first_name" in user:
                fname = user["first_name"]
            else:
                fname = ""
            if "last_name" in user:
                lname = user["last_name"]
            else:
                lname = ""
            if "city" in user:
                city = user["city"]
            else:
                city = ""
            if "nickname" in user:
                nick = user["nickname"]
            else:
                nick = ""
            usersListOutout.append(Users(fname, lname, city, nick))

# for user in usersListOutout:
#     print(user.__dict__)
#     db.post("/users", user.__dict__)

print(db.get("/users", None))