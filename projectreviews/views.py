from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import  Projects,Profile
from .serializer import ProjectsSerializer,ProfileSerializer


class PostListView(ListView):

