from django.db import models

# Create your models here.

class Match(models.Model):
    team1_pk = models.IntegerField(default=0)
    team2_pk = models.IntegerField(default=0)
