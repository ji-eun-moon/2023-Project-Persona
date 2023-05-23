from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_movie(request, movie_pk):
    movie_id = movie_pk

    # 영화 ID가 이미 존재하는지 확인
    if Movie.objects.filter(movie_id=movie_id).exists():
        return Response({'message': 'Movie already exists.'})

    # 영화 ID를 데이터베이스에 저장
    movie = Movie.objects.create(movie_id=movie_id)

    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=201)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_like(request, movie_pk):
    # 좋아요 유무와 좋아요 수 보내기
    if request.method == 'GET':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        user = request.user
        is_liked = movie.like_users.filter(pk=user.pk).exists()
        return Response({'isLiked': is_liked, 'likeCount': movie.like_users.count()})
    
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        else:
            movie.like_users.add(user)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_review(request, movie_pk):

    if request.method == 'GET':
        reviews = Review.objects.filter(movie__movie_id=movie_pk)[::-1]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            # 영화의 평균 평점 업데이트
            movie.save()
            return Response(serializer.data, status=201)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def reviews_update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    if request.method == 'DELETE':
        review = get_object_or_404(Review, pk=review_pk, movie__movie_id=movie_pk)
        if request.user == review.user:
            review.delete()
            # 영화의 평균 평점 업데이트
            movie.save()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=204)