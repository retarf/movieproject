from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.serializers import CommentSerializer
from comments.models import Comment


class TopView(APIView):

    def get(self, request, format=None):
        start_date = request.query_params['start_date']
        end_date = request.query_params['start_date']
        movies = Comment.objects.filter(created__range=[start_date, end_date]).values('movie_id').annotate(
                total_comments=Count('movie_id')
                ).order_by('-total_comments')
        number_of_comments = sorted(set(comments['total_comments'] for comments in movies), reverse=True)
        ranks = {}
        for rank, number in enumerate(number_of_comments): 
            ranks.update({number: rank + 1})
        for movie in movies: movie.update({'rank': 
            ranks[movie['total_comments']]})

        return Response(movies)
