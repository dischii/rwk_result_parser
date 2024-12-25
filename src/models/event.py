import re

class Event:
    """ Event model class """
    
    def __init__(self, gau, round_competition, league, competition_string):
        self.gau = gau
        self.round_competition = round_competition
        self.league = league
        self.competition_string = competition_string
        self.competition_day = re.search(r'\d', competition_string).group(0)
        self.competition_round = re.search(r'(Vorrunde|Rückrunde)', competition_string).group(0)

    def __str__(self):
        return f"{self.gau} - {self.round_competition} - {self.league} - {self.competition_string}"
