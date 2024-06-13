from rest_framework import status, viewsets
from rest_framework.response import Response



from drf_standardized_errors.openapi import AutoSchema

# serializer
from .serializers import UserRegistrationsSerializers

# model
from user.models import RegisterUser

# utils
from drf_standardized_errors.handler import exception_handler


# @extend_schema(tags=["Account Registration"])
class UserRegistrationView(viewsets.GenericViewSet):
    serializer_class = UserRegistrationsSerializers
    queryset = RegisterUser.objects.all()

    schema = AutoSchema()

    def get_exception_handler(self):
        return exception_handler

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    