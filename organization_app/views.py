from django.shortcuts import render
from rest_framework import generics

from .models import Department, Role
from .serializers import DepartmentSerializer, RoleSerializer


def index(request):
    context = {
        'departments': Department.objects.all(),
    }
    return render(request, 'index.html', context)


class DepartmentAPIList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class RoleAPIList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
