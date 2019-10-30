from rest_framework import serializers

from .models import Movie

class TitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
