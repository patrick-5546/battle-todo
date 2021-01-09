from django.db import models

from team.models import Player

class Todo(models.Model):
    user = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return 'Primary Key: {}'.format(self.pk)

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    completion_status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
