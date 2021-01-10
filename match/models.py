from django.db import models

# Create your models here.

class Match(models.Model):
    team1_pk = models.IntegerField(default=0)
    team2_pk = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name + ", pk={}".format(self.pk)
