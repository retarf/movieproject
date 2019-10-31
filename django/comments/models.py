from django.db import models

from movies.models import Movie

class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
