from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from hr.api.urls import urlpatterns as hr_urlpatterns

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"
urlpatterns = hr_urlpatterns
