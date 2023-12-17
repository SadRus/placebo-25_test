from django.urls import path

from .views import (
    DepartmentAPIList,
    DepartmentAPIDetailView,
    RoleAPIList,
    RoleAPIDetailView,
)


app_name = "organization_app"

urlpatterns = [
    path('departments/', DepartmentAPIList.as_view()),
    path('departments/<int:pk>/', DepartmentAPIDetailView.as_view()),
    path('roles/', RoleAPIList.as_view()),
    path('roles/<int:pk>/', RoleAPIDetailView.as_view()),
]
