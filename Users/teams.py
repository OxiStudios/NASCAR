__author__ = 'noah'

from Data.models import Racers, RaceData, RaceRacerData
from django.core.exceptions import ObjectDoesNotExist
from Users.models import Team, TeamLegacyPoints, UserProfile


#used to setup and retrieve a user's team's drivers
#also used to create a team for a user
class TeamDrivers():
    user_object = None
    team_object = None

    #takes in a UserProfile object
    def __init__(self, user_object):
        self.user_object = user_object

        #grab team object or create a new one if the user doesn't have one yet
        try:
            self.team_object = Team.objects.get(team_id=user_object.team_id)
        except ObjectDoesNotExist:
            self.team_object = Team.objects.create(team_id=user_object.team_id)

    def set_team_name(self, name):
        self.team_object.name = name
        self.team_object.save()

    def get_team_name(self):
        return self.team_object.name

    #set a driver on the team
    def set_team_driver(self, driver_id, which):
        if which is 0:
            self.team_object.racer_0_id = driver_id
            self.team_object.save()
        elif which is 1:
            self.team_object.racer_1_id = driver_id
            self.team_object.save()
        elif which is 2:
            self.team_object.racer_2_id = driver_id
            self.team_object.save()
        elif which is 3:
            self.team_object.racer_3_id = driver_id
            self.team_object.save()
        elif which is 4:
            self.team_object.racer_4_id = driver_id
            self.team_object.save()

    #returns all five drivers in the users team in a list
    def get_teams_drivers(self):
        drivers = [Racers.objects.get(racer_id=self.team_object.racer_0_id),
                   Racers.objects.get(racer_id=self.team_object.racer_1_id),
                   Racers.objects.get(racer_id=self.team_object.racer_2_id),
                   Racers.objects.get(racer_id=self.team_object.racer_3_id),
                   Racers.objects.get(racer_id=self.team_object.racer_4_id)]

        return drivers


#used to set and retrieve a user's team's points
class TeamPoints():
    user_object = None
    team_object = None

    def __init__(self, user_object):
        self.user_object = user_object
        self.team_object = Team.objects.get(team_id=user_object.team_id)

    #pushes the current points to the legacy table, before new race points are added
    def set_legacy_points(self, race_id):
        #create a new legacy points entry
        TeamLegacyPoints.objects.create(race_id_team_id=(str(race_id) + "_" + str(self.user_object.team_id)),
                                        points=self.team_object.points)

    def get_legacy_points(self, date):
        race_data = RaceData.objects.get(date=date)
        return TeamLegacyPoints.objects.get((str(race_data.race_id) + "_" + str(self.team_object.team_id)))

    #sets a user's team's current points for the season
    def set_team_points(self, race_id):
        #get the points for the each driver the user selected to start for the race that just occurred
        racer_0_rp = RaceRacerData.objects.get(
            race_id_racer_id=(str(race_id) + "_" + str(self.user_object.racer_0_set)))
        racer_1_rp = RaceRacerData.objects.get(
            race_id_racer_id=(str(race_id) + "_" + str(self.user_object.racer_1_set)))
        racer_2_rp = RaceRacerData.objects.get(
            race_id_racer_id=(str(race_id) + "_" + str(self.user_object.racer_2_set)))

        #total up the points and add them to the user's team's total points
        summed_points = (racer_0_rp + racer_1_rp + racer_2_rp) + self.team_object.points

        #set the new total and save
        self.team_object.points = summed_points
        self.team_object.save()
