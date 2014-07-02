from django.db import models


class Racers(models.Model):
    number = models.IntegerField(max_length=4)
    name = models.CharField(max_length=55)
    points = models.IntegerField(max_length=25)

    def __unicode__(self):
        return self.name


class RaceTrack(models.Model):
    track_id = models.IntegerField(max_length=5)
    location_name = models.CharField(max_length=55)
    laps = models.IntegerField(max_length=4)

    def __unicode__(self):
        return self.name

class RaceStats(models.Model):
    race_id = models.IntegerField(max_length=5)
    race_track_id = models.IntegerField(max_length=5)
    racer_number = models.IntegerField(max_length=3)
    date = models.DateField()
    won = models.IntegerField(max_length=1)
    laps_led = models.IntegerField(max_length=4)
    starting_pos = models.IntegerField(max_length=5)
    end_pos = models.IntegerField(max_length=5)

