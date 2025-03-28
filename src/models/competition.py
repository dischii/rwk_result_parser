""" This module contains the Competition class. """
import re

class Competition:
    """ This class represents a competition. """
    def __init__ (self, home_team: str, away_team: str, result: str):
        """ Initializes the competition with the given parameters. """
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        # Check if the result is in the format 'x:y'
        match = re.match(r'(\d+):(\d+)', self.result)
        if match:
            self.home_score = int(match.group(1))
            self.away_score = int(match.group(2))
        else:
            self.home_score = "N/A"
            self.away_score = "N/A"

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
