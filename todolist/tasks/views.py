from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse

from tasks.forms import TaskForm
from .models import *
from .forms import *

# Create your views here.
#Home page
def index(request):
    tasks = Task.objects.all()

    form =TaskForm()

    if(request.method == "POST"):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context={'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)

#Update Task Page
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if(request.method == "POST"):
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}

    return render(request, 'update_task.html', context)

#Delete Task Page
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item':item}
    if(request.method == "POST"):
        item.delete()
        return redirect("/")

    return render(request, 'delete_task.html', context)