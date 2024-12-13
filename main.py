import collector
from result_parser import ResultParser

collector.download_html()
parser = ResultParser()
parser.print_groups_for_team()
parser.get_results_from_team()
teams = parser.get_team_info()

print(teams)
