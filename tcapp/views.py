from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse

from .utils import *
from .models import Task
from .forms import TaskForm


class TaskCreate(ObjectCreateMixin, View):
    model_form = TaskForm
    template = 'tcapp/task_create.html'


class TaskDetail(ObjectDetailMixin, View):
    model = Task
    template = 'tcapp/task_detail.html'


class TaskUpdate(ObjectUpdateMixin, View):
    model = Task
    model_form = TaskForm
    template = 'tcapp/task_update.html'


class TaskDelete(ObjectDeleteMixin, View):
    model = Task
    templates = 'tcapp/task_delete.html'
    redirect_url = 'tasks_list_url'


def tasks_list(request):
    tasks = Task.objects.all().order_by('-date_pub')
    return render(request, 'tcapp/task_list.html', context={'tasks': tasks})


