from rest_framework import serializers

from hr import models


class DepartmentSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    sum = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.staff_set.count()

    def get_sum(self, obj):
        return obj.salary_sum()

    class Meta:
        model = models.Department
        fields = ("name", "director", "count", "sum")


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = "__all__"
