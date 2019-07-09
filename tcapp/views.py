from django.shortcuts import render

from .models import Task


def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tcapp/task_list.html', context={'tasks': tasks})


def task_detail(request, slug):
    task = Task.objects.get(slug__iexact=slug)
    return render(request, 'tcapp/task_detail.html', context={'task': task})
