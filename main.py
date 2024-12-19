""" Main file to run the program. """

import collector
from xlsx_report import XLSXReport
from result_parser import ResultParser


# Download the HTML content
collector.download_html()

# Parse the HTML content
parser = ResultParser()
parser.print_groups_for_team()
competitions = parser.get_competitions_from_team()
teams = parser.get_team_info()

# Print parsed results
print(teams)
print(competitions)

# Create a report
report = XLSXReport()
report.report_competition(competitions)
report.report_team(teams)
report.close()
