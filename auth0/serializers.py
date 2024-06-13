# serializer
from rest_framework import serializers

# model
from user.models import RegisterUser
from.models import Group


class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = "__all__"
    
   

class UserRegistrationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            "username": {"required": False, "read_only": True},
            "email": {"required": True},
            "password": {"required": True, "write_only" : True},
        }
    
    def create(self, validated_data):
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        user = RegisterUser.objects.create(email=email)
        user.set_password(validated_data.get('password'))
        user.first_name = first_name
        user.username = user.id
        user.save()
        return user