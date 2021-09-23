from rest_framework import routers

from hr.api import views

router = routers.SimpleRouter()
router.register(r"department", views.DepartmentViewSet)
router.register(r"staff", views.StaffViewSet)

urlpatterns = router.urls
