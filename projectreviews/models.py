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
    

    @property
    def design(self):
        if self.reviews.count() == 0:
            return 5
        return sum([r.design for r in self.reviews.all()]) / self.reviews.count()


    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return self.sitename

    def get_absolute_url(self):        
        return reverse('index')

class Review(models.Model):
    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, blank=True, related_name='reviews')

    def save_rate(self):
            self.save()

    def delete_rate(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('index')

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
