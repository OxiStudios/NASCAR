from django.db import models

class Racers(models.Model):
    number = models.IntegerField(4)
    name = models.CharField(55)
    points = models.IntegerField(25)

class RaceStats(models.Model):
    race_id = models.IntegerField(5)
    race_track_id = models.ForeignKey(RaceTrack.race_track_id)
    racer_number = models.ForeignKey(Racers.number)
    date = models.DateField()
    won = models.IntegerField(1)
    laps_led = models.IntegerField(4)
    starting_pos = models.IntegerField(5)
    end_pos = models.IntegerField(5)
    