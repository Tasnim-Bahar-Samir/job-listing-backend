# serializer
from rest_framework import serializers

# model
from .models import Job



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        extra_kwargs = {
            "user": {"required": True},
            "title": {"required": True, "allow_null": False},
            "type": {"required": False},
            "comapany": {"required": True, "allow_null": False},
            "location": {"required": True, "allow_null": False},
            "deadline": {"required": True, "allow_null": False},
            "salary": {"required": True, "allow_null": False},
        }
