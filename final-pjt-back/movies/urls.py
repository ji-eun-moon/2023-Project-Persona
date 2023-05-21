from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_pk>/', views.save_movie, name='save_movie'),
    path('movies/<int:movie_pk>/like/', views.movie_like, name='movie_like'),
    path('movies/<int:movie_pk>/reviews/', views.movie_review, name='movie_review'),
    path('<int:movie_pk>/reviews/<int:reviews_pk>/', views.reviews_update, name='review_update')
]
