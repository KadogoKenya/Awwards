from django.contrib import admin

# Register your models here.
from .models import Projects,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Review)

