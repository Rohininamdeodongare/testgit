import pymongo
client = pymongo.MongoClient("mongodb+srv://rohinidongare:Rohini29@rohini29.dhr2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "rohini",
    "email_" : "bantidongare29@gmail.com",
    "surname" : "dongare"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

d = {
    "name" : "rohini",
    "email_" : "bantidongare29@gmail.com",
    "surname" : "dongare"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
d = {
    "name" : "rohini",
    "email_" : "bantidongare29@gmail.com",
    "surname" : "dongare"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
d = {
    "name" : "rohini",
    "email_" : "bantidongare29@gmail.com",
    "surname" : "dongare"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)