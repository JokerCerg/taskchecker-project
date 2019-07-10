from django.shortcuts import render
from django.views.generic import View
from .utils import ObjectDetailMixin

from .models import Task
from .forms import TaskForm


def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tcapp/task_list.html', context={'tasks': tasks})


class TaskDetail(ObjectDetailMixin, View):
    model = Task
    template = 'tcapp/task_detail.html'


class TaskCreate(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'tcapp/task_create.html', context={'form': form})



