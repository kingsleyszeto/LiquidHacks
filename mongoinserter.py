import pymongo
from pymongo import MongoClient
import config
cluster = MongoClient(f"mongodb+srv://kingszeto:{config.mongo_password}@cluster0.zfror.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["rootwitch"]
collection = db["teams"]
c9 = {"_id": "c9win2020", "team": "Cloud 9", "match": "TL vs C9 NALCS Finals", "big": "cloud9", "small": "nalcs"}
tl = {"_id": "tlwin2020", "team": "Team Liquid", "match": "TL vs C9 NALCS Finals", "big": "team_liquid", "small": "nalcs"}
collection.insert_one(c9)
collection.insert_one(tl)
print(1)