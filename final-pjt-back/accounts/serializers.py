from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
from .models import Genre
from movies.models import Movie

User = get_user_model()

# 유저의 프로필 이미지
class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img', 'character')
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id',)
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_id', 'name')

class UserSerializer(serializers.ModelSerializer):
    liked_movies = MovieSerializer(many=True, read_only = True)  # 유저가 좋아하는 영화들
    genres = GenreSerializer(many=True, read_only = True) 
    
    class Meta:
        model = User
        fields = '__all__'