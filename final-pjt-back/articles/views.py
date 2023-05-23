
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from django.db.models import Count



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment_list(request,article_pk):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment,article_id=article_pk)
        # comments = Comment.objects.filter(article=article_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article,user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_pk)
        user = request.user
        is_liked = article.like_users.filter(pk=user.pk).exists()
        return Response({'isLiked': is_liked, 'likeCount': article.like_users.count()})
    
    elif request.method == 'POST':
        article = get_object_or_404(Article, id=article_pk)
        user = request.user
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            article.like_users.add(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

@api_view(['GET'])
def article_top(request):
    articles = Article.objects.annotate(like_count=Count('like_users')).order_by('-like_count')[:5]
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)