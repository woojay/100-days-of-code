import collections
import requests

MovieResults = collections.namedtuple(
    'MovieResult',
    "imdb_code, title, duration, year, rating, imdb_score, keywords, genres, director")

def find_movies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError('Search text required')

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    res = requests.get(url)
    res.raise_for_status()

    movie_data = res.json()
    movies_list = movie_data.get('hits')

    # with list comprehension
    movies = [
        MovieResults(**movie)
        for movie in movies_list
    ]

    # Sort by descending year
    movies.sort(key = lambda m: -m.year)

    return movies