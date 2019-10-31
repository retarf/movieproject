from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Comment
from .serializers import CommentSerializer


class CommentView(generics.ListCreateAPIView, mixins.ListModelMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        movie_id = self.request.query_params.get('movie_id', None)
        if movie_id is not None:
            queryset = queryset.filter(movie_id__id=movie_id)

        return queryset
