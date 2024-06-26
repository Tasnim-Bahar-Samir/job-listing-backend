from rest_framework import status, viewsets
from rest_framework.response import Response

# authentication
from rest_framework.permissions import IsAuthenticated

from auth0.permissions import IsCandidate, IsCompany

# pagination
from rest_framework.pagination import LimitOffsetPagination

# filter search sort
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from drf_standardized_errors.openapi import AutoSchema

# serializer
from .serializers import JobSerializer

# model
from .models import Job

# utils
from drf_standardized_errors.handler import exception_handler
from drf_spectacular.utils import extend_schema


class DefaultPagination(LimitOffsetPagination):
    default_limit = 50
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 50


@extend_schema(tags=["Job-list"])
class JobView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsCompany]
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filterset_fields = {
        "title": ["exact", "in"],
        "user__id": ["exact", "in"],
        "type": ["exact", "in"],
    }
    search_fields = ["title","user"]
    ordering_fields = ["title","created_at"]

    schema = AutoSchema()

    def get_exception_handler(self):
        return exception_handler

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            self.permission_classes = []
        return super().get_permissions()

    def list(self, request):
        page = self.paginate_queryset(self.filter_queryset(self.get_queryset()))
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def destroy(self, request, pk=None):
        self.get_object().delete()
        return Response(
            {"status": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
