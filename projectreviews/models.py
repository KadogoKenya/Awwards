from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    sitename = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.CharField(max_length=50)
    screenshot = models.ImageField(upload_to = 'screenshots', default = 'default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted = models.DateTimeField(auto_now_add=True)
    

    @property
    def design(self):
        if self.reviews.count() == 0:
            return 5
        return sum([r.design for r in self.reviews.all()]) / self.reviews.count()


    @property
    def usability(self):
        one = Review.objects.all().aggregate(models.Avg('usability'))['usability__avg']
        return one

    @property
    def creativity(self):
        one = Review.objects.all().aggregate(models.Avg('creativity'))['creativity__avg']
        return one

    @property
    def content(self):
        one = Review.objects.all().aggregate(models.Avg('content'))['content__avg']
        return one

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return self.sitename

    def get_absolute_url(self):        
        return reverse('index')

class Review(models.Model):
    ratings = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    design = models.IntegerField(choices=ratings, default=0)
    usability = models.IntegerField(choices=ratings, default=0)
    creativity = models.IntegerField(choices=ratings, default=0)
    content =  models.IntegerField(choices=ratings, default=0)
    overall_score = models.IntegerField(blank=True, default=0)

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
