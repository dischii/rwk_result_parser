""" This module contains the Competition class. """

class Competition:
    """ This class represents a competition. """
    def __init__ (self, home_team: str, away_team: str, result: str):
        """ Initializes the competition with the given parameters. """
        self.home_team = home_team
        self.away_team = away_team
        self.result = result

        self.home_score = int(result.split(":")[0])
        self.away_score = int(result.split(":")[1])

    def __str__(self):
        return f"{self.home_team} - {self.away_team} -> {self.result}"
    
    def to_list(self):
        """ Returns the competition as a list. """
        return [self.home_team, self.away_team, self.home_score, self.away_score]

    def check_team(self, team_name: str):
        """ Checks if the given team is part of the competition. 
        Args:
            team_name (str): The name of the team to check.
            
        Returns:
            bool: True if the team is part of the competition, False otherwise.
        """
        return team_name in self.home_team or team_name in self.away_team
