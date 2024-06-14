# serializer
from rest_framework import serializers

# model
from user.models import RegisterUser, Profile, GROUPS


   
class UserRegistrationsSerializers(serializers.ModelSerializer):
    group = serializers.ChoiceField(choices=GROUPS, write_only=True)
    class Meta:
        model = RegisterUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name','group']
        extra_kwargs = {
            "username": {"required": False, "read_only": True},
            "email": {"required": True},
            "password": {"required": True, "write_only" : True},
        }
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['group'] = instance.user_profile.group
        return representation
    
    def create(self, validated_data):
        email = validated_data.get('email')
        group = validated_data.get('group')
        print(group)
        first_name = validated_data.get('first_name')
        user = RegisterUser.objects.create(email=email)
        user.set_password(validated_data.get('password'))
        user.first_name = first_name
        user.username = user.id
        user.save()
        user_profile = user.user_profile
        user_profile.group = group
        user_profile.save()
        return user
    
    