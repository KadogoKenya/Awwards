from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Ndundiro')
        self.user.save()

        self.profile_test = Profile(user=self.user, bio='no human is limited', image='default.jpg' )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))
