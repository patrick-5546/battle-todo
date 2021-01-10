from django.db import models

from team.models import Player

class Todo(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.player.player_name + " to do list, pk={}".format(self.pk)
    

class Task(models.Model):
    todo_list = models.ForeignKey(Todo, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    completion_status = models.BooleanField(default=False)
    task_description = models.TextField(blank=True)

    def __str__(self):
        return self.task_name + ", pk={}".format(self.pk)
