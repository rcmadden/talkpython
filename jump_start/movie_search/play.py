import collections
import requests

MovieResult = collections.namedtuple(
    'MovieResult',
    'Type, Year, Title, imdbID, Poster'
)

search = 'capital'
url ='http://www.omdbapi.com/?s={}&y=&plot=full&r=json'.format(search)

r = requests.get(url)
data = r.json()
results = data['Search']

# print(results[0]['Poster'])

# movies = []
# for result in results:
#     m = MovieResult(**result)
#     movies.append(m)

movies = (
    MovieResult(**m)
    for m in results
)
