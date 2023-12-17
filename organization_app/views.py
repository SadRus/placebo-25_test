from django.shortcuts import render
from rest_framework import generics

from .models import Department
from .serializers import DepartmentSerializer


def index(request):
    context = {
        'departments': Department.objects.all(),
    }
    return render(request, 'index.html', context)


class DepartmentAPIList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


def roles_list_api(request):
    pass
