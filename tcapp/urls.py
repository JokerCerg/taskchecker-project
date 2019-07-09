from django.urls import path
from .views import *


urlpatterns = [
    path('', tasks_list, name='tasks_list_url'),
    path('task/<str:slug>/', task_detail, name='task_detail_url'),
]