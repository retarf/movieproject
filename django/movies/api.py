from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TitleSerializer, MovieSerializer
from .models import Movie
from .src.api_requests import title_request
from .src.handlers import keys_to_lower
from .src.db_requests import save_movie


class MovieView(APIView):

    def post(self, request, format=None):
        title_serializer = TitleSerializer(data=request.data)
        if title_serializer.is_valid():
            title = title_serializer.data['title']
            data = title_request(title)
            movie = save_movie(data)
            movie_serializer = MovieSerializer(movie)
        else:
            return Response(title_serializer.errors)
            
        return Response(movie_serializer.data)

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


