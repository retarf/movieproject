from rest_framework import serializers

from .models import Comment

"""
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
"""

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie_id', 'content')

