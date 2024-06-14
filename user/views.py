from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# pagination
from rest_framework.pagination import LimitOffsetPagination

# filter search sort
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_standardized_errors.openapi import AutoSchema

# authentication
from rest_framework.permissions import IsAuthenticated
from auth0.permissions import IsCandidate

# utils
from drf_standardized_errors.handler import exception_handler
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound

# model
from .models import RegisterUser
from job.models import SavedJob

# serializer
from .serializers import (
    UserProfileSerializer,
    SavedJobSerializers
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
        print(self.kwargs["pk"],str(self.request.user.id))
        if self.kwargs["pk"] != str(self.request.user.id):
            print('hello')
            raise NotFound()
        return RegisterUser.objects.get(id=self.request.user.id)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["User saved jobs."])
class SavedJobView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated,IsCandidate]
    serializer_class = SavedJobSerializers
    queryset = SavedJob.objects.all()
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filterset_fields = {
        "job": ["exact", "in"],
    }
    search_fields = ["job"]
    ordering_fields = ["created_at"]

    schema = AutoSchema()

    def get_exception_handler(self):
        return exception_handler

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


    def list(self, request):
        serializer = self.get_serializer(
            self.filter_queryset(self.get_queryset()), many=True
        )
        page = self.paginate_queryset(self.filter_queryset(self.get_queryset()))
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.get_object().delete()
        return Response(
            {"status": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
