from django.shortcuts import render


def tasks_list(request):
    return render(request, 'tcapp/task_list.html')