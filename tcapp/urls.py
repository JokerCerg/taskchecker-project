from django.urls import path
from .views import *


urlpatterns = [
    path('', tasks_list)
]