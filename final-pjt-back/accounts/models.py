from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

# class Genre(models.Model):
#     genre_id = models.IntegerField(unique=True)

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img = models.TextField(blank=True, null=True)
    character = models.IntegerField(blank=True, null=True)
    # genres = models.ManyToManyField(Genre, blank=True)