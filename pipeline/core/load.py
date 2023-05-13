from core import date, b_date
import pymongo
import os

from dotenv import load_dotenv
load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

def load(df):
    client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.srokaih.mongodb.net/?retryWrites=true&w=majority".format(username,password))
    db = client["cinepool"]
    collection = db["media"]
    collection.insert_many(df)
    collection.delete_many({"date": {"$eq": b_date}})

    print("Successfully loaded data into MongoDB")