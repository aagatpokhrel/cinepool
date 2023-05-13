from sentence_transformers import SentenceTransformer
from core import date

model = SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')


def transform_description(description):
    embeddings = model.encode(description)
    return embeddings
    
def splice_description(description):
    #only take the first sentence
    return description.split('.')[0]

def merge_transform(df):
    movie_dictionary = df[0]
    show_dictionary = df[1]
    #specify type of media
    all_data = []

    for k,v in movie_dictionary.items():
        movie_data = {}
        first_plot = splice_description(v['description'])
        movie_data['name'] = k
        movie_data['type'] = 'movie'
        movie_data['date'] = date
        movie_data['genres'] = v['genres']
        movie_data['description'] = first_plot
        movie_data['desc_embedding'] = transform_description(first_plot)
        all_data.append(movie_data)

    for k,v in show_dictionary.items():
        show_data = {}
        first_plot = splice_description(v['description'])
        show_data['name'] = k
        show_data['type'] = 'show'
        show_data['date'] = date
        show_data['genres'] = v['genres']
        show_data['description'] = first_plot
        show_data['desc_embedding'] = transform_description(first_plot)
        all_data.append(show_data)
    
    return all_data

def transform(df):
    df = merge_transform(df)
    return df
