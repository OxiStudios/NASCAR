__author__ = 'noah'

from Users.models import Team, League

class LeagueCalculator():

    user_object = None
    league_object = None
    team_object = None

    def __init__(self, user_object):
        self.user_object = user_object
        self.team_object = Team.objects.get(team_id=user_object.team_id)
        self.league_object = League.objects.get(league_id=self.team_object.team_id)

    #returns a list of the teams in a given league, listed by highest to lowest points
    def league_short_highest(self):
        team_qs = Team.objects.filter(league_id=self.league_object.league_id).order_by('points')
        return team_qs

    #lets the user know how many points they need to get to the next place in their league
    def points_to_position(self):
        pass