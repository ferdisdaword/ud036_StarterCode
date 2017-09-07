# Movie Trailer Website
This will create a Movie Trailer Website after a list of movies is added to the `entertainment_center.py`

## Prerequisites
TMDB API wrapper _tmdbsimple_ is needed to use this program
_tmdbsimple_ is available on the [Python Package Index (PyPI)](https://pypi.python.org/pypi/tmdbsimple)

You can install _tmdbsimple_ using one of the following techniques.
* Use pip:
```
pip install tmdbsimple
```
* Download the .zip or .tar.gz file from PyPI and install it yourself
* Download the [source from Github](http://github.com/celiao/tmdbsimple) and install it yourself

If you install it yourself, also install [requests](http://www.python-requests.org/en/latest).
More information on TMDB API Key and _tmdbsimple_ examples located on [official tmdbsimple Github](https://github.com/celiao/tmdbsimple)

## Download the code to clone or run
You can download the code by [direct download](https://github.com/ferdisdaword/ud036_StarterCode/archive/master.zip) or running the below command (assuming you have git installed):

```
git clone https://github.com/ferdisdaword/ud036_StarterCode.git
```

## Run the code
Once you have added your movie items and created your list, run the below command:
```
python entertainment_center.py
```
This will create the Movie Trailer website HTML file to be used for your website.

## Examples
### Movie List Item
To create a movie list item to display on the website in the `entertainment_center.py` file, it might look something like this:

```
my_movie_name = tmdb.Movie(id_from_tmdb_url)
my_movie_name.info()
my_movie_name.releases()
my_movie_name.video()
```
You will then want to add it to the _movies_ list:
```
movies = [my_movie_name]
```
### To store more movie related information
This can be done by updating the movie class within the `fresh_tomatoes.py` file using TMDB API _tmdbsimple_ Movie class. 
**Some examples** of the current information being stored per movie:
```
content += movie_tile_content.format(
    movie_title=movie.title,
    movie_storyline=movie.overview,
    poster_image_url=movie.poster_path,
    trailer_youtube_id=trailer_youtube_id,
    movie_rating=rating)

return content
```
