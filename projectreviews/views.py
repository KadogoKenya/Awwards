from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Review,Comments
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import MerchSerializer,profileSerializer
from users.models import Profile
from .forms import NewProjectForm,ReviewForm, VotesForm
from django.contrib.auth.decorators import login_required


class ProjectCreateView(LoginRequiredMixin,CreateView):
    
    model = Project
    fields = ['sitename', 'description', 'url', 'screenshot']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectListView(ListView):
    model = Project
    template_name = 'award/index.html'
    context_object_name = 'projects'
    ordering = ['-submitted']

def projects(request,project_id):
    try:
        projects = Project.objects.get(id=project_id)
        all_ratings = Review.objects.filter(project=project_id)
    except Exception as e:
        raise Http404()
    # single user votes count
    count = 0
    for i in all_ratings:
        count+=i.usability
        count+=i.design
        count+=i.content
    if count > 0:
        average = round(count/3,1)
    else:
        average = 0
    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project_id
            rate.save()
        return redirect('projects',project_id)
    else:
        form = VotesForm()
    # The votes logic
    votes = Review.objects.filter(project=project_id)
    usability = []
    design = []
    content = []
    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content)
    if len(usability) > 0 or len(design)>0 or len(content)>0:
        average_usability = round(sum(usability)/len(usability),1)
        average_design = round(sum(design)/len(design),1)
        average_content = round(sum(content)/len(content),1)
        average_rating = round((average_content+average_design+average_usability)/3,1)
    else:
        average_content=0.0
        average_design=0.0
        average_usability=0.0
        average_rating = 0.0
    '''
    To make sure that a user only votes once
    '''
    arr1 = []
    for use in votes:
        arr1.append(use.user_id)
    auth = arr1
    reviews = ReviewForm(request.POST)
    if request.method == 'POST':
        if reviews.is_valid():
            comment = reviews.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect ('projects',project_id)
        else:
            reviews = ReviewForm()
    user_comments = Comments.objects.filter(project_id=project_id)
    context = {
        'projects':projects,
        'form':form,
        'usability':average_usability,
        'design':average_design,
        'content':average_content,
        'average_rating':average_rating,
        'auth':auth,
        'all_ratings':all_ratings,
        'average':average,
        'comments':user_comments,
        'reviews':reviews,
    }
    return render(request,'award/project_reviews.html',context)


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

@login_required(login_url='/login/')
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
    