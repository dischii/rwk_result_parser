""" This script extracts and prints the results of a competition from an HTML file. """

import re
from bs4 import BeautifulSoup
from team import Team
from competition import Competition

# Load the HTML content
with open('output.html', 'r', encoding='utf-8') as file:
    content = file.read()

def print_result(cells: list):
    """ Prints the result of a competition. """
    comp = Competition(cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip())
    if comp.check_team("SV Wappersdorf"):
        print(comp)

def get_league_name_from_table_header(header: str):
    """ Extracts the league name from the given table header """
    return re.search(r'Tabelle der (.*?) ------', header).group(1)

def print_groups_for_team(parsed_html: BeautifulSoup, team_name):
    """ Prints the groups for the given team. """
    tables = parsed_html.find_all('table', {'style': 'width:100%'})
    for table in tables:
        header = table.find('th', colspan="3")
        if header:
            print(header.text)
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) > 1:
                    team = cells[0].text.strip()
                    if team_name in team:
                        print(team)

def get_team_info(soup):
    """ Extracts and prints the team information from the given HTML content. """
    tables = soup.find_all('table', {'style': 'width:100%'})
    for table in tables:
        header = table.find('th', colspan="3")
        if header:
            league = get_league_name_from_table_header(header.text)
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) > 1:
                    team = cells[0].text.strip()
                    if "SV Wappersdorf" in team:
                        placement = team.split(".")[0]
                        team_name = team.split(".")[1]
                        points = cells[1].text.strip()
                        cut = cells[2].text.strip()
                        print(Team(league, team_name, int(placement), points, cut))

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Filter the results for the fight between SG Freystadt 1 and SV Wappersdorf 1
fight_results = soup.find_all('table', {'style': 'width:100%;'})

# Extract and print the relevant information
for table in fight_results:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('th')
        if len(cells) == 3:
            print_result(cells)

# Find and return the table containing the specified header
print_groups_for_team(soup, "SV Wappersdorf")

get_team_info(soup)
