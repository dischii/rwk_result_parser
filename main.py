""" Main file to run the program. """
import os
import collector

from xlsx_report import XLSXReport
from result_parser import ResultParser
from md_report import MDReport

# Download the HTML content
html_result = collector.download_html()

for html in html_result:
    # Parse the HTML content
    parser = ResultParser(html)
    events = parser.get_event_infos()
    competitions = parser.get_competitions_from_team()
    teams = parser.get_team_info()

    # Create Markdown
    mdfilename = os.path.basename(html).split(".")[0]
    mdfilename = f"svw-results/docs/results_{mdfilename}"
    md = MDReport(mdfilename, f"{events[0].competition_string}")
    md.report_competition(competitions)
    md.report_team(teams)
    md.add_file_links("files/report.xlsx", "Excel Report")
    md.create_file()

    # Create a report
    report = XLSXReport(filename=html.replace("html", "xlsx"), header=f"Results from {events[0].competition_string}")
    report.report_competition(competitions)
    report.report_team(teams)
    report.close()
