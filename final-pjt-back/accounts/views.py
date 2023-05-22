from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserImgSerializer

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

@api_view(['POST'])
def follow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
            followed = False
        else:
            user.followers.add(request.user)
            followed = True
    context = {
        'followed' : followed,
    }
    serializer = UserSerializer(user)
    return Response(serializer.data)