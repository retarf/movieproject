from django.db.models import Count
from rest_framework import generics

from comments.serializers import CommentSerializer
from comments.models import Comment


class TopView(generics.ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.annotate(
                movie_count=Count('movie_id')
                ).order_by('movie_count')

