#this site extracts data from the imdb site by crawling using beautiful soup

import requests
from bs4 import BeautifulSoup
from core import date

shows_url = "https://www.imdb.com/calendar/?ref_=rlm&region=US&type=TV"
movies_url = "https://www.imdb.com/calendar/?region=us"


def crawl_url(url):
    url = "https://www.imdb.com" + url
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    description = 0
    genres = []
    try:
        description = soup.find('span',{'data-testid': 'plot-xl'})
        description = description.text
    except:
        pass

    try:
        genres = []
        find_genres = soup.find_all('span',{'class': 'ipc-chip__text'})
        for genre in find_genres:
            genres.append(genre.text)
    except:
        pass
    return genres[:-1], description
    
def parse_article(soup):
    objects = {}
    article = soup.find('article',{'data-testid': 'calendar-section'})
    release_date = soup.find('div',{'data-testid': 'release-date'})
    if (release_date.text != date):
        return objects
    try:
        a_tags = article.find_all('a',{'role': 'button'})
        for a_tag in a_tags:
            title = a_tag.text
            if (title!=''):
                url = a_tag.get('href')
                genres, descriptions = crawl_url(url)
                objects[title] = {'genres': genres, 'description': descriptions}
            else:
                continue
    except AttributeError:
        pass
    return objects
    

def extract():
    response_movies = requests.get(movies_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup_movies = BeautifulSoup(response_movies.content, 'html.parser')

    response_shows = requests.get(shows_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup_shows = BeautifulSoup(response_shows.content, 'html.parser')
    
    movie_dictionary = parse_article(soup_movies)
    show_dictionary = parse_article(soup_shows)

    df = [movie_dictionary, show_dictionary]
    return df