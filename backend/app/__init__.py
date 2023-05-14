from flask import Flask
from flask_cors import CORS
import pymongo
import os
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['SECRET_KEY'] = "cinepool"
app.config['CORS_HEADERS'] = 'Content-Type'

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")


client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.srokaih.mongodb.net/?retryWrites=true&w=majority".format(username,password))
db = client["cinepool"]
collection = db["media"]

from app import routes