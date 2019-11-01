from django_rest import serializers

from comments.serializers import CommentSerializer
from comments.models import Comment

class TopSerializer(serializers.ModelSerializer):
    def get_ranks(self, sorted_movies):
        return {score: place + 1 for place, score in enumerate(sorted_movies)}
    def get_queryset(self):
        movies = Comment.objects.values('movie_id').annotate(total_comments=Count('movie_id'))
        sorted_movies = sorted(set(comments['total_comments'] for comments in movies), reverse=True)
        raiting = {score: place + 1 for place, score in enumerate(sorted_movies)}


