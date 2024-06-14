from rest_framework import serializers

# model
from .models import RegisterUser,Profile
from job.models import SavedJob

from django.contrib.auth.models import User

# serializers
from job.serializers import JobSerializer


# assets

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [ 'group']
        extra_kwargs = {
            'user' : {'required': False},
            'group' : {'required': False},
        }


class UserProfileSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(required=True)
    class Meta:
        model = RegisterUser
        fields = ['id', 'first_name', 'last_name', 'email', 'user_profile']
        
    
class SavedJobSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "job": {"required": True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.job:
            data["job"] = JobSerializer(
                instance.job, context=self.context
            ).data
        return data