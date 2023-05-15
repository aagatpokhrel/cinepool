from app import collection
import sentence_transformers
import numpy as np

def return_embeddings(description):
    #analyze description
    model = sentence_transformers.SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')
    embeddings = model.encode(description)
    arr_list = [float(x) if isinstance(x, np.float32) else x for x in embeddings.tolist()]
    return arr_list

def search_db(data):
    #search for movies/shows
    search_query = {}
    try:
        search_query['type'] = data['type']
    except:
        pass

    try:
        search_query['genres'] = data['genres']
    except:
        pass

    try:
        search_query['date'] = data['date']
    except:
        pass
    
    documents = collection.find(search_query)

    if (data['description']):
        embedding = return_embeddings(data['description'])

    for document in documents:
        print (document)

