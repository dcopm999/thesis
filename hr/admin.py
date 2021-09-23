from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from hr import models


class StaffInline(AdminImageMixin, admin.StackedInline):
    model = models.Staff


@admin.register(models.Department)
class DepartmentAdmin(MPTTModelAdmin):
    inlines = [StaffInline]
    list_display = ("name", "director")
    list_display_links = ("name",)


@admin.register(models.Staff)
class StaffAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "department", "position")
