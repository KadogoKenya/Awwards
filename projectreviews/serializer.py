from rest_framework import serializers
from .models import Project
from users.models import Profile
from .models import MoringaMerch


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('sitename','description','url','screenshot','user','submitted')

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'user')