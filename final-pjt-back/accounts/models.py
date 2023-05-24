from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    genre_id = models.IntegerField(unique=True)

class User(AbstractUser):
    profile_img = models.TextField(blank=True, null=True)
    character = models.IntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)