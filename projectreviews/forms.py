from django import forms
from .models import Project,Comments,Review

# from . import forms
#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['description','sitename','screenshot','url']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comments']

class VotesForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['usability','design','content']
