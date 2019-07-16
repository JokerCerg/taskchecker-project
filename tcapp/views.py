from django.shortcuts import render
from django.views.generic import View

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

    # def get(self, request, slug):
    #     task = Task.objects.get(slug__iexact=slug)
    #     bound_form = TaskForm(initial={'title': task.title, 'body': task.body})
    #     return render(request, 'tcapp/task_update.html', context={'form': bound_form, 'task': task})
    #
    # def post(self, request, slug):
    #     task = Task.objects.get(slug__iexact=slug)
    #     bound_form = TaskForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_task = bound_form.save()
    #         return redirect(new_task)
    #     return render(request, 'tcapp/task_update.html', context={'form': bound_form, 'task': task})

# class TaskDelete(View):
#     def get(self, request, slug):


def tasks_list(request):
    tasks = Task.objects.all().filter()
    return render(request, 'tcapp/task_list.html', context={'tasks': tasks})


