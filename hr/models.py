from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from sorl.thumbnail import ImageField


class Department(MPTTModel):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Name"))
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    director = models.ForeignKey(
        "hr.staff",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="director",
        verbose_name=_("Director"),
    )

    def salary_sum(self):
        return self.staff_set.aggregate(sum=Sum("salary")).get("sum")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class Staff(models.Model):
    photo = ImageField(upload_to="photos/staff/", verbose_name=_("Photo"))
    first_name = models.CharField(max_length=100, verbose_name=_("First name"))
    middle_name = models.CharField(max_length=100, verbose_name=_("Middle name"))
    last_name = models.CharField(
        max_length=100, db_index=True, verbose_name=_("Last name")
    )
    position = models.CharField(max_length=100, verbose_name=_("Position"))
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Salary")
    )
    date_birth = models.DateField(verbose_name=_("Birth day"))
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, verbose_name=_("Department")
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = _("Staff")
        verbose_name_plural = _("Staff")
        unique_together = [["first_name", "middle_name", "last_name", "department"]]
