from django.urls import path

from .views import departments_list_api, roles_list_api


app_name = "organization_app"

urlpatterns = [
    path('departments/', departments_list_api),
    path('roles/', roles_list_api),
]
