from django.db import models

# Create your models here.


class Task(models.Model):
    todo_item = models.CharField(max_length=50)
    task_completed = models.BooleanField(default=False)

