from .models import Project
#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }