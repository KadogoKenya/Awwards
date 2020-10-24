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


class Review(models.Model):
    ratings = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='reviews')
    design = models.IntegerField(choices=ratings, default=0)
    usability = models.IntegerField(choices=ratings, default=0)
    creativity = models.IntegerField(choices=ratings, default=0)
    content =  models.IntegerField(choices=ratings, default=0)
    overall_score = models.IntegerField(blank=True, default=0)

