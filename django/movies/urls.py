from django.urls import path

from . import api

app_name = 'movies'
urlpatterns = [
    path('', api.MovieView.as_view(), name='index'),
]
