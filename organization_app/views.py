from django.shortcuts import render

from .models import Department


def index(request):
    context = {
        'departments': Department.objects.all(),
    }
    return render(request, 'index.html', context)
