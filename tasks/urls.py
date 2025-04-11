from django.urls import path
from .views import task_list, task_create, task_edit, task_delete, task_toggle

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/new/', task_create, name='task_create'),
    path('task/edit/<int:pk>/', task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', task_delete, name='task_delete'),
    path('task/toggle/<int:pk>/', task_toggle, name='task_toggle'),
]