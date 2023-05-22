from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
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

class UserSerializer(serializers.ModelSerializer):
    liked_movies = MovieSerializer(many=True, read_only = True)  # 유저가 좋아하는 영화들

    class Meta:
        model = User
        fields = '__all__'