from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Review
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import MerchSerializer,profileSerializer
from users.models import Profile
from .forms import NewProjectForm

# from .models import  MoringaMerch

# def index(request):
#     return render(request, 'award/index.html')


class ProjectCreateView(LoginRequiredMixin,CreateView):
    
    model = Project
    fields = ['sitename', 'description', 'url', 'screenshot']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectListView(ListView):
    model = Project
    template_name = 'award/index.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-submitted']

class ReviewCreateView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ['design', 'usability', 'creativity', 'content']

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Project` instance exists
        before going any further.
        """
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)

class ProjectDetailView(DetailView):
    model = Project
    
class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializer = MerchSerializer(all_merch, many=True)
        return Response(serializer.data)

class profileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = profileSerializer(all_profile, many=True)
        return Response(serializers.data)

# @login_required(login_url='/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})
    