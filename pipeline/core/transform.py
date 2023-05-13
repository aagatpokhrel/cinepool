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
    all_data = {}

    for k,v in movie_dictionary.items():
        first_plot = splice_description(v['description'])
        all_data['name'] = k
        all_data['type'] = 'movie'
        all_data['date'] = date
        all_data['genres'] = v['genres']
        all_data['description'] = first_plot
        all_data['desc_embedding'] = transform_description(first_plot)

    for k,v in show_dictionary.items():
        first_plot = splice_description(v['description'])
        all_data['name'] = k
        all_data['type'] = 'show'
        all_data['date'] = date
        all_data['genres'] = v['genres']
        all_data['description'] = first_plot
        all_data['desc_embedding'] = transform_description(first_plot)

    return all_data

def transform(df):
    df = merge_transform(df)
    print (df)
    return df
