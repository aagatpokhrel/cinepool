from core import date, b_date
import pymongo

def load(df):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["cinepool"]
    collection = db["media"]
    collection.insert_many(df)
    collection.delete_many({"date": {"$eq": b_date}})

    print("Successfully loaded data into MongoDB")