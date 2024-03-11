from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList

def todolist(request):
    todos = ToDoList.objects.all()
    return render(request, 'app/index.html', {'todos': todos})

def createtodo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        ToDoList.objects.create(title=title, description=description)
    return redirect('todolist')

def completetodo(request, todo_id):
    todo = ToDoList.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todolist')

def deletetodo(request, todo_id):
    todo = get_object_or_404(ToDoList, id=todo_id)
    todo.delete()
    return redirect('todolist')