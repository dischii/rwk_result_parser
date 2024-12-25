""" Main file to run the program. """

import collector
from xlsx_report import XLSXReport
from result_parser import ResultParser
from md_report import MDReport


# Download the HTML content
#collector.download_html()

# Parse the HTML content
parser = ResultParser()
events = parser.get_event_infos()
parser.print_groups_for_team()
competitions = parser.get_competitions_from_team()
teams = parser.get_team_info()

# Print parsed results
print(events[0].competition_string)
print(teams)
print(competitions)

# Create Markdown
md = MDReport(f"svw-results/docs/results_{events[0].competition_day}", f"{events[0].competition_string}")
md.report_competition(competitions)
md.report_team(teams)
md.add_file_links("files/report.xlsx", "Excel Report")
md.create_file()

# Create a report
report = XLSXReport()
report.report_competition(competitions)
report.report_team(teams)
report.close()
