from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie')


class MovieSerializer(serializers.ModelSerializer):
    reviews_set = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews_set.count', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

