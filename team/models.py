from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_points = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_points = models.IntegerField(default=0)
    player_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_special_select = models.BooleanField(default=False)
    physical_attack = models.IntegerField(default=0)
    physical_defense = models.IntegerField(default=0)
    special_attack = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name