import fresh_tomatoes
import tmdbsimple as tmdb

tmdb.API_KEY = 'ec601831e85b21fd8aab487b60a875e7'

# Movie instances for tmdb API used by fresh_tomatoes.py
# movie = tmdb.Movies(id) - Load the movie id from tmdb.org to tmdb API
# movie.info() - Request information for movie id
# movie.releases() - Provide release information with ratings certifications
# movie.videos() - Provide location to the youtube id for the trailer video

brotherhood = tmdb.Movies(6312)
brotherhood.info()
brotherhood.releases()
brotherhood.videos()

hanna = tmdb.Movies(50456)
hanna.info()
hanna.releases()
hanna.videos()

kingsman = tmdb.Movies(207703)
kingsman.info()
kingsman.releases()
kingsman.videos()

scouts_guide = tmdb.Movies(273477)
scouts_guide.info()
scouts_guide.releases()
scouts_guide.videos()

turbo_kid = tmdb.Movies(310135)
turbo_kid.info()
turbo_kid.releases()
turbo_kid.videos()

warriors_way = tmdb.Movies(46528)
warriors_way.info()
warriors_way.releases()
warriors_way.videos()

movies = [brotherhood, hanna, kingsman, scouts_guide, turbo_kid, warriors_way]

fresh_tomatoes.open_movies_page(movies)
