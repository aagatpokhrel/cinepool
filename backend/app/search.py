from app import collection
import sentence_transformers
import numpy as np

def return_embeddings(description):
    #analyze description
    model = sentence_transformers.SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')
    embeddings = model.encode(description)
    arr_list = [float(x) if isinstance(x, np.float32) else x for x in embeddings.tolist()]
    return arr_list



def search(data):
    #search for movies/shows
    search_query = {}
    if (data['type']):
        search_query['type'] = data['type']
    if (data['genres']):
        search_query['genres'] = data['genres']
    if (data['date']):
        search_query['date'] = data['date']
    
    documents = collection.find(search_query)

    if (data['description']):
        embedding = return_embeddings(data['description'])

    print(documents)

