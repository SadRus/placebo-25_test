from django.urls import path

from .views import roles_list_api, DepartmentAPIList


app_name = "organization_app"

urlpatterns = [
    path('departments/', DepartmentAPIList.as_view()),
    path('roles/', roles_list_api),
]
