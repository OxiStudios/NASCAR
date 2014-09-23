from django.test import TestCase

# Create your tests here.


def calculate_driver_points(end_pos, laps_led, won, most_laps_led):
        starting_total_points = 43
        #race_racer_data = RaceRacerData.objects.get(race_id_racer_id=(str(race_id) + "_" + str(racer.number)))

        #subtract one point from starting total for each place they were behind first
        points = starting_total_points - end_pos + 1
        #add a point per lap led
        points += laps_led
        #add 5 points for a win
        if won:
            points += 5
        #add a point if they have most laps led
        if most_laps_led:
            points += 1

        print points


calculate_driver_points(end_pos=3, laps_led=2, won=False, most_laps_led=False)