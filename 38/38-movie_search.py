import pprint as pp
import requests
import requests.exceptions

import collections
import movie_svc


def get_movie_data(search):

    MovieResults = collections.namedtuple(
        'MovieResult',
        "imdb_code, title, duration, year, rating, imdb_score, keywords, genres, director")

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

    res = requests.get(url)
    # res.raise_for_status()
    movie_data = res.json()
    movies_list = movie_data.get('hits')

    # with list comprehension
    movies = [
        MovieResults(**movie)
        for movie in movies_list
    ]

    # movies = []
    # for movie in movies_list:
    #     m = MovieResults(**movie)  # key word args
    #     movies.append(m)

    for movie in movies:
        print('{} - {}'.format(movie.year, movie.title))


def search_event_loop():
    search = 'capital'

    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} movies".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()

        except ValueError:
            print('Error: Search text is required.')
        except requests.exceptions.ConnectionError:
            print('Error: Connection Error')
        except requests.exceptions.ConnectTimeout:
            print('Error: Connection Timedout')
        except Exception as e:
            print('Error: '.format(e))

    print('Exiting... ')


def print_header():
    print('---------------------------')
    print('     Movie Search APP')
    print('---------------------------')
    print()


def main():
    print_header()
    search_event_loop()

if __name__ == '__main__':
    main()
