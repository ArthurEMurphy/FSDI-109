
import pymongo
import certifi


con_str = "mongodb+srv://murphman185:tcS8DG3hTssytC@cluster0.vfpd3.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("berry")
