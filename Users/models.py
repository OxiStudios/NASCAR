from django.db import models

class User(models.Model):
    user_id = models.IntegerField(25)
    user_name = models.CharField(55)
    password = models.CharField(44)
    team_id = models.ForeignKey(Team.team_id)


class Team(models.Model):
    team_id = models.IntegerField(25)
    league_id = models.ForeignKey(League.league_id)
    points = models.IntegerField(25)

    racer_0_ID = models.IntegerField(25)
    racer_1_ID = models.IntegerField(25)
    racer_2_ID = models.IntegerField(25)
    racer_3_ID = models.IntegerField(25)
    racer_4_ID = models.IntegerField(25)


class League(models.Model):
    league_id = models.IntegerField(25)
    name = models.CharField(20)
    points = models.IntegerField(25)