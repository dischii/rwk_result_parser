""" This module creates a markdown report. """
from mdutils.mdutils import MdUtils

# # --------------------------------------------------------------
# # testdata

# from src.models.event import Event
# from src.models.competition import Competition
# from src.models.team import Team

# event = Event(
#       "Schützengau Altdorf - Neumarkt - Beilngries", 
#       "Rundenschießen Luftgewehr  2025", 
#       "Gauoberliga", 
#       "Ergebnisse des 1. Wettkampftages der Vorrunde"
#       )

# comps_for_report = []

# comps_for_report.append(Competition("SG Freystadt 1", "SV Wappersdorf 1", "1465:1489"))
# comps_for_report.append(Competition("SV Reichertshofen 2", "SV Wappersdorf 2", "1481:1493"))
# comps_for_report.append(Competition("SV Wappersdorf 3", "SV Sulzkirchen 1", "1401:1416"))
# comps_for_report.append(Competition("SV Wappersdorf 4", "SV Wolfstein 3", "1392:1316"))
# comps_for_report.append(Competition("SV Wappersdorf 5", "SV Hirschberg 2", "1322:1328"))
# comps_for_report.append(Competition("SV Woffenbach 1", "SV Wappersdorf 2", "1045:909"))
# comps_for_report.append(Competition("SV Wappersdorf 1", "SV Woffenbach 2", "964:991"))

# teams_for_report = []
# teams_for_report.append(Team("Gauliga 1", "SV Wappersdorf 1", 2, "2:0", 1489.00))
# teams_for_report.append(Team("Gauliga 2", "SV Wappersdorf 2", 1, "2:0", 1493.00))
# teams_for_report.append(Team("A-Klasse 1", "SV Wappersdorf 3", 10, "0:2", 1401.00))
# teams_for_report.append(Team("B-Klasse 2", "SV Wappersdorf 4", 1, "2:0", 1392.00))
# teams_for_report.append(Team("B-Klasse 2", "SV Wappersdorf 5", 7, "0:2", 1322.00))
# teams_for_report.append(Team("Gauoberliga", "SV Wappersdorf 1", 7, "0:2", 964.00))
# teams_for_report.append(Team("Gauoberliga", "SV Wappersdorf 2", 8, "0:2", 909.00))

# # --------------------------------------------------------------

class MDReport:
    """ This class creates a report in md format. """
    def __init__(self, filename: str = 'report.md', title: str = 'RWK Results'):
        """ Initializes the report with the given filename. """
        self.mdfile = MdUtils(file_name=filename)
        self.mdfile.new_header(level=1, title=title)
        print(f"{self.mdfile.file_name} initialized.")

    def report_competition(self, competitions: list):
        """ Returns the competition as a list. """
        self.mdfile.new_header(level=2, title='Competitions')
        self.mdfile.write('The following competitions have been found:')
        self.mdfile.new_line()

        comp_list = ["Home Team", "Away Team", "Home Score", "Away Score"]
        for comp in competitions:
            comp_list.extend(comp.to_list())

        self.mdfile.new_table(columns=4, rows= len(competitions) + 1, text=comp_list, text_align='center')
        self.mdfile.new_line()

    def report_team(self, teams: list):
        """ Returns the team as a list. """
        self.mdfile.new_header(level=2, title='Teams')
        self.mdfile.write('The following teams have been found:')
        self.mdfile.new_line()

        team_list = ["League", "Team", "Position", "Result", "Score"]
        for team in teams:
            team_list.extend(team.to_list())

        self.mdfile.new_table(columns=5, rows= len(teams) + 1, text=team_list, text_align='center')
        self.mdfile.new_line()

    def report_shooter(self, shooters: list):
        """ Returns the shooters as a list. """
        adult_shooters = [shooter for shooter in shooters if "Jugendklasse" not in shooter.discipline]
        self.mdfile.new_header(level=2, title='Shooters')
        self.mdfile.write('The following shooters have been found:')
        self.mdfile.new_line()

        shooter_list = ["Name", "Score", "Team", "Discipline", "League"]
        # sort shooters by score
        adult_shooters.sort(key=lambda x: x.score, reverse=True)
        for shooter in adult_shooters:
            shooter_list.extend(shooter.to_list())

        self.mdfile.new_table(columns=5, rows= len(adult_shooters) + 1, text=shooter_list, text_align='center')
        self.mdfile.new_line()

        # extract shooters where discipline includes Jugendklasse
        youth_shooters = [shooter for shooter in shooters if "Jugendklasse" in shooter.discipline]
        self.mdfile.new_header(level=2, title='Jugendklassse')
        self.mdfile.write('The following shooters have been found in the Jugendklasse:')
        self.mdfile.new_line()

        youth_shooter_list = ["Name", "Score", "Team", "Discipline", "League"]
        # sort shooters by score
        youth_shooters.sort(key=lambda x: x.score, reverse=True)
        for shooter in youth_shooters:
            youth_shooter_list.extend(shooter.to_list())
        
        self.mdfile.new_table(columns=5, rows= len(youth_shooters) + 1, text=youth_shooter_list, text_align='center')
        self.mdfile.new_line()


    def add_file_links(self, link: str, text: str):
        """ Adds a link to the given file. """
        self.mdfile.new_line('Downloadable file:' + self.mdfile.new_inline_link(link=link, text=text))

    def create_file(self):
        """ Creates the markdown file. """
        self.mdfile.create_md_file()
