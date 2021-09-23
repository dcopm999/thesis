from django.urls import path

from thesis.users import views as user_views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_views.user_redirect_view, name="redirect"),
    path("~update/", view=user_views.user_update_view, name="update"),
    path("<str:username>/", view=user_views.user_detail_view, name="detail"),
]
