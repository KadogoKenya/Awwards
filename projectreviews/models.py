from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    description = models.CharField(max_length=250)
    sitename = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    screenshot = models.ImageField(upload_to = 'screenshots', default = 'default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE ,blank=True)
    submitted = models.DateTimeField(auto_now_add=True)

    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)    


    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return self.sitename

    def get_absolute_url(self):        
        return reverse('index')

class Review(models.Model):
    design=models.PositiveIntegerField(default=0)
    usability=models.PositiveIntegerField(default=0)
    content=models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.IntegerField(default=0)


    def save_rate(self):
            self.save()

    def delete_rate(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('index')

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField(max_length=400)     
    project_id = models.IntegerField(default=0) 


class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)


