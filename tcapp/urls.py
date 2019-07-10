from django.urls import path
from .views import *


urlpatterns = [
    path('', tasks_list, name='tasks_list_url'),
    path('task/create', TaskCreate.as_view(), name='task_create_url'),
    path('task/<str:slug>/', TaskDetail.as_view(), name='task_detail_url'),
]