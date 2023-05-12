
def transform_description(description):
    pass

def merge_transform(df):
    movie_dictionary = df[0]
    show_dictionary = df[1]
    #specify type of media
    movie_dictionary = {k: {'genres': v['genres'], 'description': v['description'], 'desc_embedding':transform_description(v['description']) ,'type': 'movie'} for k, v in movie_dictionary.items()}
    show_dictionary = {k: {'genres': v['genres'], 'description': v['description'], 'description': v['description'], 'desc_embedding':transform_description(v['description']) ,'type': 'show'} for k, v in show_dictionary.items()}
    #merge the two dictionaries
    movie_dictionary.update(show_dictionary)
    return movie_dictionary


def transform(df):
    df = merge_transform(df)
    return df
