from django.shortcuts import render, redirect

from .models import Movie

# Create your views here.
def movie_like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_user.add(request.user)
    return redirect()

def movie_review(request):
    pass