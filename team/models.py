from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_points = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name + ", pk={}".format(self.pk)

class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_points = models.IntegerField(default=0)
    player_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_special_select = models.BooleanField(default=False)
    has_attacked = models.BooleanField(default=False)
    damage_dealt = models.FloatField(default=0.0)
    todo_points = models.IntegerField(default=0)
    physical_attack = models.IntegerField(default=1)
    physical_defense = models.IntegerField(default=1)
    special_attack = models.IntegerField(default=1)
    special_defense = models.IntegerField(default=1)
    speed = models.IntegerField(default=1)

    def __str__(self):
        return self.player_name + ", pk={}".format(self.pk)
