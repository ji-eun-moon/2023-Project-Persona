from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile, name="profile"),
    path('upload_image/<username>/', views.upload_image, name="upload_image"),
    path('genres/<username>/', views.user_genres, name="user_genres")
]