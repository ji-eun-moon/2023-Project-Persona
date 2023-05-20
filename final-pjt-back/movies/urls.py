from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:pk>/like/', views.movie_like, name='movie_like'),
    path('movies/<int:pk>/reviews/', views.movie_review, name='movie_review'),
]
