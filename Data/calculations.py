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