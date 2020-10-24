from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    profile_picture=models.ImageField(upload_to='users/', default='user.png')
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(default='Review')





