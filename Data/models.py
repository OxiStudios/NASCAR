from django.db import models


class Racers(models.Model):
    number = models.IntegerField(max_length=4)
    name = models.CharField(max_length=55)
    points = models.IntegerField(max_length=25)
    wins = models.IntegerField(max_length=2)

    def __unicode__(self):
        return self.name


class Averages(models.Model):
    racer_id = models.IntegerField(max_length=4)
    a_start_pos = models.DecimalField(decimal_places=2, max_digits=5)
    a_end_pos = models.DecimalField(decimal_places=2, max_digits=5)
    a_points_per_race = models.DecimalField(decimal_places=2, max_digits=5)


class RaceTrack(models.Model):
    track_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=55)
    track_length = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.name


class RaceRacerData(models.Model):
    race_id_racer_id = models.IntegerField(max_length=15)
    won = models.IntegerField(max_length=1)
    laps_led = models.IntegerField(max_length=4)
    starting_pos = models.IntegerField(max_length=5)
    end_pos = models.IntegerField(max_length=5)


class RaceData(models.Model):
    race_id = models.IntegerField(max_length=6)
    track = models.ForeignKey(RaceTrack)
    date = models.DateField()
    laps = models.IntegerField(max_length=4)

