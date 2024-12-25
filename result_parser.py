""" This class extracts and prints the results of a competition  or team infos from an HTML file. """

import re
from bs4 import BeautifulSoup
from src.models.team import Team
from src.models.competition import Competition
from src.models.event import Event

class ResultParser:
    """ This class is used to parse the HTML content of the RWK shooting website. """
    def __init__(self):
        """ Initializes the ResultParser with the given HTML content.
            Requriement: The HTML content must be stored in a file called 'output.html'.
        """
        self.__load_file()
        # Parse the HTML content with BeautifulSoup
        self.soup = BeautifulSoup(self.content, 'html.parser')


    def __load_file(self, file_name = "output.html"):
        """ Load the HTML content from the given file. """
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"Error: The file {file_name} was not found.")
            self.content = ""
        except IOError:
            print(f"Error: An error occurred while reading the file {file_name}.")
            self.content = ""

    def print_result(self, cells: list, team_name: str):
        """ Prints the result of a competition. """
        comp = Competition(cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip())
        if comp.check_team(team_name):
            print(comp)

    def get_league_name_from_table_header(self, header: str):
        """ Extracts the league name from the given table header """
        return re.search(r'Tabelle der (.*?) ------', header).group(1)

    def print_groups_for_team(self, team_name: str = "SV Wappersdorf"):
        """ Prints the groups for the given team. """
        tables = self.soup.find_all('table', {'style': 'width:100%'})
        for table in tables:
            header = table.find('th', colspan="3")
            if header:
                print(header.text)
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) > 1:
                        team = cells[0].text.strip()
                        if team_name.strip() == team.split(".")[1].strip():
                            print(team)

    def get_team_info(self, team_name: str = "SV Wappersdorf"):
        """ Extracts and prints the team information from the given HTML content. 
        Returns a list of found teams. 
        
        Args:
            team_name (str): The name of the team to search for.
                Currently not used - the team name is hardcoded.
                This depends to an unsolved problem with searching substring in bs4 elements.

        Returns:
            list: A list of found teams.
        """
        tables = self.soup.find_all('table', {'style': 'width:100%'})
        found_teams = []
        for table in tables:
            header = table.find('th', colspan="3")
            if header:
                league = self.get_league_name_from_table_header(header.text)
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) > 1:
                        team = cells[0].text.strip()
                        # TODO: use variable instead of hardcoded team name
                        # it's necesary to use the string because the variable can not be used to check
                        # if substring is in team variable.
                        # # team seems to be a class from beautifulsoup and not a string
                        if "SV Wappersdorf" in team:
                            teaminstance = Team(league, team.split(".")[1], int(team.split(".")[0]), cells[1].text.strip(), cells[2].text.strip())
                            print(teaminstance)
                            found_teams.append(teaminstance)
        return found_teams

    def get_competitions_from_team(self, team_name: str = "SV Wappersdorf"):
        """ Prints the results of the competition.

        Args:
            team_name (str): The name of the team to search for.
                Default: "SV Wappersdorf"

        Returns:
            list: A list of found competitions. 
        """
        fight_results = self.soup.find_all('table', {'style': 'width:100%;'})
        found_competitions = []
        for table in fight_results:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('th')
                if len(cells) == 3:
                    comp = Competition(cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip())
                    if comp.check_team(team_name):
                        found_competitions.append(comp)
                        print(comp)
        return found_competitions

    def get_event_infos(self):
        """ Extracts the event information from the HTML content. 
        
        Returns:
            list: A list of Event objects
        """
        # Find the span element with the text "Ergebnisse"
        result_elements = self.soup.find_all('span', string=re.compile("Ergebnisse"))
        event_infos = []
        for span_element in result_elements:
            # Find the parent element of the span element to get infos about the competition day
            par_element = span_element.parent
            infos = par_element.find_all('span')
            event_infos.append(Event(infos[0].text.strip(), infos[1].text.strip(), infos[2].text.strip(), infos[3].text.strip()))

        return event_infos
