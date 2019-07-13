from django.shortcuts import render, redirect
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

    def post(self, request):
        bound_form = TaskForm(request.POST)

        if bound_form.is_valid():
            new_task = bound_form.save()
            return redirect(new_task)
        return render(request, 'tcapp/task_create.html', context={'form': bound_form})

