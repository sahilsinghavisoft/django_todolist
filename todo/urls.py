from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('create/', views.createtodo, name='createtodo'),
    path('complete/<int:todo_id>/', views.completetodo, name='completetodo'),
    path('delete/<int:todo_id>/', views.deletetodo, name='deletetodo'), 
]