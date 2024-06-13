from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# pagination
from rest_framework.pagination import LimitOffsetPagination


# authentication
from rest_framework.permissions import IsAuthenticated


# utils
from drf_standardized_errors.handler import exception_handler
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound


# model
from .models import RegisterUser


# serializer
from .serializers import (
    UserProfileSerializer,
)

class DefaultPagination(LimitOffsetPagination):
    default_limit = 50
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 50

@extend_schema(tags=["User Profile"])
class UserProfileView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = RegisterUser.objects.all()
    pagination_class = DefaultPagination

    def get_exception_handler(self):
        return exception_handler
    
    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = []
        return super().get_permissions()

    def get_object(self):
        if self.kwargs["pk"] != str(self.request.user.id):
            raise NotFound()
        return RegisterUser.objects.get(id=self.request.user.id)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)