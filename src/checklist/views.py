from django.shortcuts import render
from .models import Task


def homepage(request):
    checklist = Task.objects.all()
    todo_items = [obj.todo_item for obj in checklist]

    context = {'arr': todo_items}
    return render(request, "home.html", context)
