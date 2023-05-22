from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile, name="profile"),
    path('follow/<username>/', views.follow, name="follow"),
    path('upload_image/<username>/', views.upload_image, name="upload_image"),
]