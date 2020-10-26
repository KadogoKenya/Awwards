from . import views 
from django.urls import path
from django.conf.urls import url
from .views import  ProjectCreateView, ProjectListView, ReviewCreateView, ProjectDetailView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('', ProjectListView.as_view(), name='index'),
    path('review/new/<int:pk>/', ReviewCreateView.as_view(), name='review-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    url(r'^new/project$', views.new_project, name='new-project')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
