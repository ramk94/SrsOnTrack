from django.shortcuts import render
from .models import Task
from .forms import TaskCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TaskCreateForm()

    checklist = Task.objects.all()
    context = {'form': form, 'arr': checklist}
    return render(request, "home.html", context)


def delete_task(request, id):
    # if request.method == "POST":
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect("/")


def complete_task(request, id):
    item = Task.objects.get(id=id)
    item.task_completed = True
    item.save()
    return HttpResponseRedirect("/")
