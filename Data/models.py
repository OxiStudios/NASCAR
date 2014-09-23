from django.db import models


#holds each racer's basic data
class Racers(models.Model):
    number = models.IntegerField(max_length=4)
    name = models.CharField(max_length=55)
    points = models.IntegerField(max_length=25)
    wins = models.IntegerField(max_length=2)
    data_added = models.IntegerField(max_length=1)

    def __unicode__(self):
        return self.name


#holds each racer's averages for the season
class Averages(models.Model):
    racer_id = models.IntegerField(max_length=4)
    a_start_pos = models.DecimalField(decimal_places=2, max_digits=5)
    a_end_pos = models.DecimalField(decimal_places=2, max_digits=5)
    a_points_per_race = models.DecimalField(decimal_places=2, max_digits=5)
    a_laps_led_per_race = models.DecimalField(decimal_places=2, max_digits=5)


#holds each track's static data
class RaceTrack(models.Model):
    track_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=55)
    track_length = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.location_name


#hold all the data for each racer in every race that has happened this season
class RaceRacerData(models.Model):
    race_id_racer_id = models.CharField(max_length=6)

    #used for the filter in summing up stats
    racer_id = models.IntegerField(max_length=4)

    won = models.BooleanField()
    laps_led = models.IntegerField(max_length=4)
    most_laps_led = models.BooleanField()
    starting_pos = models.IntegerField(max_length=5)
    end_pos = models.IntegerField(max_length=5)
    total_points = models.IntegerField(max_length=4)


#hold the race information for each race
class RaceData(models.Model):
    race_id = models.IntegerField(max_length=6)
    track = models.ForeignKey(RaceTrack)
    date = models.DateField()
    laps = models.IntegerField(max_length=4)


#saves the amount of races that have happened this season
#saves when new data has been synced
class MetaStats(models.Model):
    #used to grab the row, value=1
    default_id = models.IntegerField(max_length=1)
    date_time_synced = models.DateTimeField()
    latest_race_id = models.IntegerField(max_length=5)