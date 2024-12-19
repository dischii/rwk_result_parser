""" class for team information """

class Team:
    """ class for team information """
    def __init__(self, league:str, name: str, placement: int, points: str, cut: str):
        """ init function 
        Args:
            league (str): league of the team
            name (str): name of the team
            placement (int): placement of the team
            points (int): points of the team
            cut (str): cut of the team
        """
        self.league = league
        self.name = name
        self.placement = placement
        self.points = points
        self.cut = cut

    def __str__(self):
        return f"[{self.league}] \t {self.name} \t {self.placement}. Platz \t {self.points} - {self.cut}"

    def __repr__(self):
        return f"[{self.league}] \t {self.name} \t {self.placement}. Platz \t {self.points} - {self.cut}"

    def to_list(self):
        """ Returns the team as a list. """
        return [self.league, self.name, self.placement, self.points, self.cut]
