from django import forms
from .models import Project

# from . import forms
#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # exclude = ['submitted']
        fields=['description','sitename','screenshot','url']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }