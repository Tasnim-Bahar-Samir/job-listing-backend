from rest_framework import status, viewsets, parsers, renderers
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.views.generic import View



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
    