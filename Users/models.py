from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    team_id = models.AutoField(primary_key=True)

    current_race = models.DateField()

    racer_0_set = models.IntegerField(max_length=1)
    racer_1_set = models.IntegerField(max_length=1)
    racer_2_set = models.IntegerField(max_length=1)

    def __unicode__(self):
        return self.user.username


class UserHistory(models.Model):
    team_id = models.IntegerField(max_length=7)

    race_date = models.DateField()

    racer_selected_0_ID = models.IntegerField(max_length=3)
    racer_selected_1_ID = models.IntegerField(max_length=3)
    racer_selected_2_ID = models.IntegerField(max_length=3)


class Team(models.Model):
    team_id = models.IntegerField(max_length=7)
    league_id = models.IntegerField(max_length=7)
    name = models.CharField(max_length=8)
    points = models.IntegerField(max_length=25)

    racer_0_ID = models.IntegerField(max_length=3)
    racer_1_ID = models.IntegerField(max_length=3)
    racer_2_ID = models.IntegerField(max_length=3)
    racer_3_ID = models.IntegerField(max_length=3)
    racer_4_ID = models.IntegerField(max_length=3)


class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    points = models.IntegerField(max_length=25)