from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserImgSerializer
from .models import Genre
# Create your views here.

@api_view(['GET'])
def profile(request, username):
  user = get_object_or_404(get_user_model(), username=username)
  if request.method == 'GET':
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
@api_view(['GET', 'PUT'])
def upload_image(request, username):
  user = get_object_or_404(get_user_model(), username=username)
  
  if request.method == 'GET':
        serializer = UserImgSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == 'PUT':
      if request.user != user:
          return Response({'profile':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

      serializer = UserImgSerializer(user, data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def user_genres(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method =='POST':
        user = get_object_or_404(get_user_model(), username=username)
        if request.user != user:
            return Response({'profile':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        genre_ids = request.data.get('genre_ids', [])
        # 기존에 저장된 장르 초기화 및 선택한 장르 추가
        user.genres.clear()
        for genre_id in genre_ids:
            genre = get_object_or_404(Genre, genre_id=genre_id)
            user.genres.add(genre)
        
        serializer = UserSerializer(user)  # 유저 시리얼라이저를 통해 응답 데이터 직렬화
        return Response(serializer.data)
    