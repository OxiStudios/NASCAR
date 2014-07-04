__author__ = 'noah'
from Users.models import Team, League, LeagueLegacyPoints, UserHistory, UserProfile
from Users.teams import TeamUpdater
from Data.models import MetaStats, RaceData
import datetime


#used to check if the user's league and team is fully updated when the user logs in
#assumes that the user is apart of a league and team
class UpdateChecker():
    user_object = None
    team_object = None
    league_object = None
    meta_stats_object = None

    race_id = 0

    def __init__(self, user_object, race_id):
        self.user_object = user_object
        self.team_object = Team.objects.get(team_id=self.user_object.team_id)
        self.league_object = League.objects.get(league_id=self.team_object.league_id)
        self.meta_stats_object = MetaStats.objects.get(default_id=1)

        self.race_id = race_id

    #checks if user's league is updated
    def check_league_sync(self):
        database_sync_time = self.meta_stats_object.date_time_synced
        league_sync_time = self.league_object.date_time_synced

        #league data is not synced
        if database_sync_time > league_sync_time:
            league_updater = LeagueUpdater(league_object=self.league_object, race_id=self.race_id)

            league_updater.update_league()

            #league data is now synced
            league_updater.sync_finished()
            self.league_object.date_time_synced = datetime.datetime.now()
            self.league_object.save()
        #league data already is synced
        else:
            pass


#used to update user history and racers set for upcoming race
class UserUpdater():
    user_object = None

    def __init__(self, user_object):
        self.user_object = user_object

    #set a racer to start for that week
    def set_selected_racer(self, which, racer_id):
        if which is 0:
            self.user_object.racer_0_set = racer_id
            self.user_object.save()
        elif which is 1:
            self.user_object.racer_1_set = racer_id
            self.user_object.save()
        elif which is 2:
            self.user_object.racer_2_set = racer_id
            self.user_object.save()

    #when league sync, clear selected racers from last week and add to UserHistory
    def update_user_history(self, race_id):

        race_data_object = RaceData.objects.get(race_id=race_id)
        date = race_data_object.date

        racer_id_0 = self.user_object.racer_0_set
        racer_id_1 = self.user_object.racer_1_set
        racer_id_2 = self.user_object.racer_2_set

        new_history_entry = UserHistory(team_id=self.user_object.team_id, race_date=date,
                                        racer_selected_0_id=racer_id_0, racer_selected_1_id=racer_id_1,
                                        racer_selected_2_id=racer_id_2)
        new_history_entry.save()


#used to update the teams in a league
class LeagueUpdater():
    league_object = None
    race_id = 0

    def __init__(self, league_object, race_id):
        self.league_object = league_object
        self.race_id = race_id

    def update_league(self):
        #QuerySet of the teams in the current league
        league_team_qs = Team.objects.filter(league_id=self.league_object.league_id)
        new_league_points = 0

        #create a new league legacy points entry
        LeagueLegacyPoints.objects.create(
            race_id_league_id=(str(self.race_id) + "_" + str(self.league_object.league_id)),
            points=self.league_object.points)

        #for each team in the QuerySet, update the stats of them
        for team_object in league_team_qs:
            #update each team's stats in the league
            team_updater = TeamUpdater(team_object=team_object, race_id=self.race_id)
            team_updater.update_team_stats()
            #total up points for league points
            new_league_points += team_object.points
            #reset and save legacy user data
            user_object = UserProfile.objects.get(team_id=team_object.team_id)
            user_updater = UserUpdater(user_object=user_object)
            user_updater.update_user_history(race_id=self.race_id)

        #update league points
        self.league_object.points = new_league_points
        self.league_object.save()

    def sync_finished(self):
        self.league_object.synced = True
        self.league_object.save()