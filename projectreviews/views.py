from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import  Projects,Profile
from .serializer import ProjectsSerializer,ProfileSerializer

class PostListView(ListView):
    model=Projects
    template_name='index.html'
    context_object_name='projects'
    ordering=['-created_date']

class PostDetailView(DetailView):
    model = Projects

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    success_url = '/'
    fields =['author','image','description', 'title' ,'link']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = Projects
    success_url = '/'
    fields =['author','image','description', 'title' ,'link']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author_profile:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Projects
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author_profile:
            return True
        return False


