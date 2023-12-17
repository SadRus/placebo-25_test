from django.urls import path

from .views import RoleAPIList, DepartmentAPIList


app_name = "organization_app"

urlpatterns = [
    path('departments/', DepartmentAPIList.as_view()),
    path('roles/', RoleAPIList.as_view()),
]
