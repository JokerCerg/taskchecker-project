from django.shortcuts import render, redirect
from django.views.generic import View
from .utils import *

from .models import Task
from .forms import TaskForm


def tasks_list(request):
    tasks = Task.objects.all().filter()
    return render(request, 'tcapp/task_list.html', context={'tasks': tasks})


class TaskDetail(ObjectDetailMixin, View):
    model = Task
    template = 'tcapp/task_detail.html'


class TaskCreate(ObjectCreateMixin, View):
    model_form = TaskForm
    template = 'tcapp/task_create.html'


