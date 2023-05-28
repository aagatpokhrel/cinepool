from app import collection
import sentence_transformers
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from bson import ObjectId


def return_embeddings(description):
    #analyze description
    model = sentence_transformers.SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')
    embeddings = model.encode(description).reshape(1, -1)
    arr_list = [float(x) if isinstance(x, np.float32) else x for x in embeddings.tolist()]
    return arr_list

def search_description(documents, description):
    #search for description

    target_key = "desc_embedding"
    # Retrieve values for the target key from all documents
    values = [doc.get(target_key) for doc in documents if target_key in doc]

    embedding = return_embeddings(description)

    nbrs = NearestNeighbors(n_neighbors= 2, algorithm='brute').fit(values)
    distances, indices = nbrs.kneighbors(embedding)
    
    print (indices)
    results = []
    for i in indices[0]:
        results.append(dict(documents[i]))
    
    for result in results:
        for key, value in result.items():
            if key== 'desc_embedding':
                result[key] = 'matched'
            if isinstance(value, ObjectId):
                result[key] = str(value)

    return results

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
    
    documents = list(collection.find(search_query))

    if (data['description']):
        lists = search_description(documents, data['description'])
        return lists
    else:
        return documents

