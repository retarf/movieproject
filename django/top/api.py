from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.serializers import CommentSerializer
from comments.models import Comment


class TopView(APIView):

    def get(self, request, format=None):
        params = request.query_params
        if params.get('start_date', None) is not None  and params.get('end_date', None) is not None:
            start_date = request.query_params['start_date']
            end_date = request.query_params['start_date']
            movies = Comment.objects.filter(created__range=[start_date, end_date]).values('movie_id').annotate(
                    total_comments=Count('movie_id')
                    ).order_by('-total_comments')

        elif params.get('start_date', None) is not None:
            start_date = request.query_params['start_date']
            movies = Comment.objects.filter(created__gte=start_date).values('movie_id').annotate(
                    total_comments=Count('movie_id')
                    ).order_by('-total_comments')

        elif params.get('end_date', None) is not None:
            end_date = request.query_params['start_date']
            movies = Comment.objects.filter(created__lte=end_date).values('movie_id').annotate(
                    total_comments=Count('movie_id')
                    ).order_by('-total_comments')

        else:
            movies = Comment.objects.values('movie_id').annotate(
                    total_comments=Count('movie_id')
                    ).order_by('-total_comments')

        number_of_comments = sorted(set(comments['total_comments'] for comments in movies), reverse=True)
        ranks = {}
        for rank, number in enumerate(number_of_comments): 
            ranks.update({number: rank + 1})
        for movie in movies: movie.update({'rank': 
            ranks[movie['total_comments']]})

        return Response(movies)
