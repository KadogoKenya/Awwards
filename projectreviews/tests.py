from django.test import TestCase
from .models import Projects,Profile,Review
# Create your tests here.


class ProjectsTestClass(TestCase):
    def setUp(self):
        self.description=Projects(location='description')

    def test_instance(self):
        self.assertTrue(isinstance(self.description,Projects))

    def tearDown(self):
        Projects.objects.all().delete()

    def test_save_method(self):
        self.description.save_location()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.description.delete_location('description')
        projects = Projects.objects.all()
        self.assertTrue(len(projects)==0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile()
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    
