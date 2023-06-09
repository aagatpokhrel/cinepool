from app import app,collection
from flask import jsonify, request

from app.search import search_db
import json


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get_movies', methods=['GET', 'POST'])
def get_movies():
    documents = collection.find()
    return documents

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        results = search_db(data)
        return jsonify(results)
    else:
        return jsonify({"message":"Error"})