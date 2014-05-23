from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    team_bank = models.CharField(max_length=30)


class Driver(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    car_number = models.CharField(max_length=4)


class Location(models.Model):

    name = models.CharField(max_length=30)
    length = models.IntegerField()


class Race(models.Model):
    location = models.CharField(max_length=30)

