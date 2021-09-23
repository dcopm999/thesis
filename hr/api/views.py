from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from hr import models
from hr.api import serializers


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StaffSerializer
    queryset = models.Staff.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("last_name", "department")
