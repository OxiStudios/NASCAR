from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    team_id = models.AutoField(primary_key=True)

    racer_0_set = models.IntegerField(max_length=3)
    racer_1_set = models.IntegerField(max_length=3)
    racer_2_set = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.user.username


class UserHistory(models.Model):
    team_id = models.IntegerField(max_length=7)

    race_date = models.DateField()

    racer_selected_0_ID = models.IntegerField(max_length=3)
    racer_selected_1_ID = models.IntegerField(max_length=3)
    racer_selected_2_ID = models.IntegerField(max_length=3)


class TeamLegacyPoints(models.Model):

    race_id_team_id = models.CharField(max_length=10)
    points = models.IntegerField(max_length=6)


class LeagueLegacyPoints(models.Model):

    race_id_league_id = models.CharField(max_length=10)
    points = models.IntegerField(max_length=6)


class Team(models.Model):
    team_id = models.IntegerField(max_length=7)
    league_id = models.IntegerField(max_length=7)
    name = models.CharField(max_length=8)
    points = models.IntegerField(max_length=25)

    racer_0_id = models.IntegerField(max_length=3)
    racer_1_id = models.IntegerField(max_length=3)
    racer_2_id = models.IntegerField(max_length=3)
    racer_3_id = models.IntegerField(max_length=3)
    racer_4_id = models.IntegerField(max_length=3)

    synced = models.BooleanField()
    date_time_synced = models.DateTimeField()


class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    points = models.IntegerField(max_length=25)

    synced = models.BooleanField()
    date_time_synced = models.DateTimeField()