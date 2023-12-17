from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Department
from .serializers import DepartmentSerializer


def index(request):
    context = {
        'departments': Department.objects.all(),
    }
    return render(request, 'index.html', context)


@api_view(['GET', 'POST'])
def departments_list_api(request):
    if request.method == "GET":
        departments = Department.objects.all()
        department_serializer = DepartmentSerializer(
            departments,
            many=True,
        )
        return Response(department_serializer.data)

    if request.method == "POST":
        department_serializer = DepartmentSerializer(data=request.data)
        department_serializer.is_valid(raise_exception=True)
        department_serializer.save()
        return Response(department_serializer.data)


def roles_list_api(request):
    pass
