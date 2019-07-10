from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Task
from django.views.generic import View
from .utils import ObjectDetailMixin


def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tcapp/task_list.html', context={'tasks': tasks})


class TaskDetail(ObjectDetailMixin, View):
    model = Task
    template = 'tcapp/task_detail.html'


