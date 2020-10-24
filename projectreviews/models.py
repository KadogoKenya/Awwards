from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Projects(models.Model):
    image = models.ImageField(upload_to='profile_pics/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    link = models.URLField()
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='1', blank = True)

class Profile(models.Model):
    profile_picture=models.ImageField(upload_to='users/', default='user.png')
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(default='Review')

