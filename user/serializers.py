from rest_framework import serializers

# model
from .models import RegisterUser,Profile
from django.contrib.auth.models import User

# serializers
from auth0.serializers import GroupSerializer

# assets

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'group']
        extra_kwargs = {
            'user' : {'required': False},
            'group' : {'read_only': True},
        }


    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['group'] = GroupSerializer(instance.group.all(), many=True).data
        return data
    



class UserProfileSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(required=True)
    class Meta:
        model = RegisterUser
        fields = ['first_name', 'last_name', 'email', 'user_profile']