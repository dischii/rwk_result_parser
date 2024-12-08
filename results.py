from bs4 import BeautifulSoup
import re

# Load the HTML content
# with open('/C:/Users/alexd/Documents/Projekte/GitHub/rwk_ergebnisse/output.html', 'r', encoding='utf-8') as file:
with open('output.html', 'r', encoding='utf-8') as file:
    content = file.read()

def print_result(cells: list):
    home_team = cells[0].text.strip()
    away_team = cells[1].text.strip()
    result = cells[2].text.strip()
    
    if home_team.startswith("SV Wappersdorf") or away_team.startswith("SV Wappersdorf"):
        print(f"{home_team} - {away_team} -> {result}")

def get_league_name_from_table_header(header: str):
    league_name = re.search(r'Tabelle der (.*?) ------', header).group(1)
    return (league_name)  # Output: Gauliga 1

def print_groups_for_team(soup, team_name):
    tables = soup.find_all('table', {'style': 'width:100%'})
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
                        print(f"[{league}] \t {team_name} \t {placement}. Platz \t {points} - {cut}")
    

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
