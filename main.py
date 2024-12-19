""" Main file to run the program. """

import collector
from result_parser import ResultParser

# Download the HTML content
collector.download_html()

# Parse the HTML content
parser = ResultParser()
parser.print_groups_for_team()
parser.get_results_from_team()
teams = parser.get_team_info()

# Print the teams
print(teams)
