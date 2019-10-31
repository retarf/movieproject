from django.db import models

# Create your models here.

'''
{'Title': 'Batman',
 'Year': '1989',
 'Rated': 'PG-13',
 'Released': '23 Jun 1989',
 'Runtime': '126 min',
 'Genre': 'Action, Adventure',
 'Director': 'Tim Burton',
 'Writer': 'Bob Kane (Batman characters), Sam Hamm (story), Sam Hamm (screenplay), Warren Skaaren (screenplay)',
 'Actors': 'Michael Keaton, Jack Nicholson, Kim Basinger, Robert Wuhl',
 'Plot': 'The Dark Knight of Gotham City begins his war on crime with his first major enemy being the clownishly homicidal Joker.',
 'Language': 'English, French, Spanish',
 'Country': 'USA, UK',
 'Awards': 'Won 1 Oscar. Another 8 wins & 26 nominations.',
 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_SX300.jpg',
 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.5/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '72%'},
  {'Source': 'Metacritic', 'Value': '69/100'}],
 'Metascore': '69',
 'imdbRating': '7.5',
 'imdbVotes': '317,478',
 'imdbID': 'tt0096895',
 'Type': 'movie',
 'DVD': '25 Mar 1997',
 'BoxOffice': 'N/A',
 'Production': 'Warner Bros. Pictures',
 'Website': 'N/A',
 'Response': 'True'}
'''

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=20)
    rated = models.CharField(max_length=100)
    released = models.CharField(max_length=20)
    runtime = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=400)
    actors = models.CharField(max_length=500)
    plot = models.CharField(max_length=500)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.CharField(max_length=200)
    poster = models.CharField(max_length=300)
    ratings = models.CharField(max_length=500)
    metascore = models.CharField(max_length=50)
    imdbrating = models.CharField(max_length=20)
    imdbvotes = models.CharField(max_length=50)
    imdbid = models.CharField(max_length=50)
    movie_type = models.CharField(max_length=50)
    dvd = models.CharField(max_length=20)
    boxoffice = models.CharField(max_length=50)
    production = models.CharField(max_length=200)
    website = models.CharField(max_length=500)
    response = models.CharField(max_length=10)

    def __str__(self):
        return self.title
