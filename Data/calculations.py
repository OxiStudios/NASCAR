__author__ = 'noah'

from models import Averages, RaceRacerData, Racers
from django.db.models import Sum, Count


class RacerUpdater():
    def __init__(self):
        pass

    def update_driver_averages(self, racer):
        averages = Averages.objects.get(racer_id=racer.number)
        racer_id = racer.number
        new_win_total = 0

        #grab total count of a given stat
        amount = RaceRacerData.objects.filter(racer_id=racer_id).aggregate(Count('a_start_pos'))

        #sum up the stats and assign them to a new total
        new_a_start_pos = RaceRacerData.objects.filter(racer_id=racer_id).aggregate(Sum('a_start_pos')) / amount

        new_a_end_pos = RaceRacerData.objects.filter(racer_id=racer_id).aggregate(Sum('a_end_pos')) / amount

        new_a_points_per_race = RaceRacerData.objects.filter(racer_id=racer_id).aggregate(
            Sum('a_points_per_race')) / amount

        a_laps_led_per_race = RaceRacerData.objects.filter(racer_id=racer_id).aggregate(
            Sum('a_laps_led_per_race')) / amount

        new_win_total += RaceRacerData.objects.get(racer_id=racer_id).win

        #update old averages with new averages
        averages.a_start_pos = new_a_start_pos
        averages.a_end_pos = new_a_end_pos
        averages.a_points_per_race = new_a_points_per_race
        averages.a_laps_led_per_race = a_laps_led_per_race
        averages.save()

        #update old wins with new wins
        racer.wins = new_win_total
        racer.save()

    def update_all_drivers_average(self):

        #a QuerySet of the drivers
        racer_qs = Racers.objects.all()

        for racer in racer_qs:
            self.update_driver_averages(racer=racer)

    def calculate_driver_points(self, racer, race_id):
        starting_total_points = 43
        race_racer_data = RaceRacerData.objects.get(race_id_racer_id=(str(race_id) + "_" + str(racer.number)))

        #subtract one point from starting total for each place they were behind first
        points = starting_total_points - race_racer_data.end_pos + 1
        #add a point per lap led
        points += race_racer_data.laps_led
        #add 5 points for a win
        if race_racer_data.won:
            points += 5
        #add a point if they have most laps led
        if race_racer_data.most_laps_led:
            points += 1

        #set and save the points for the current driver
        race_racer_data.total_points = points
        race_racer_data.save()

    def calculate_all_drivers_points(self, race_id):

        racers_qs = Racers.objects.all()

        for racer in racers_qs:
            self.calculate_driver_points(racer=racer, race_id=race_id)