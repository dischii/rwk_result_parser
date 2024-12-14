""" This module creates a report file in xlsx format. """ 

import xlsxwriter

import xlsxwriter.worksheet
from competition import Competition
from team import Team

# testdata - TODO: replace test data with acutal data from results.py
comps_for_report = []


comps_for_report.append(Competition("SG Freystadt 1", "SV Wappersdorf 1", "1465:1489"))
comps_for_report.append(Competition("SV Reichertshofen 2", "SV Wappersdorf 2", "1481:1493"))
comps_for_report.append(Competition("SV Wappersdorf 3", "SV Sulzkirchen 1", "1401:1416"))
comps_for_report.append(Competition("SV Wappersdorf 4", "SV Wolfstein 3", "1392:1316"))
comps_for_report.append(Competition("SV Wappersdorf 5", "SV Hirschberg 2", "1322:1328"))
comps_for_report.append(Competition("SV Woffenbach 1", "SV Wappersdorf 2", "1045:909"))
comps_for_report.append(Competition("SV Wappersdorf 1", "SV Woffenbach 2", "964:991"))

teams_for_report = []
teams_for_report.append(Team("Gauliga 1", "SV Wappersdorf 1", 2, "2:0", 1489.00))
teams_for_report.append(Team("Gauliga 2", "SV Wappersdorf 2", 1, "2:0", 1493.00))
teams_for_report.append(Team("A-Klasse 1", "SV Wappersdorf 3", 10, "0:2", 1401.00))
teams_for_report.append(Team("B-Klasse 2", "SV Wappersdorf 4", 1, "2:0", 1392.00))
teams_for_report.append(Team("B-Klasse 2", "SV Wappersdorf 5", 7, "0:2", 1322.00))
teams_for_report.append(Team("Gauoberliga", "SV Wappersdorf 1", 7, "0:2", 964.00))
teams_for_report.append(Team("Gauoberliga", "SV Wappersdorf 2", 8, "0:2", 909.00))

    

def report_competition(ws: xlsxwriter.worksheet, start_row: int, comp_list: list):
    """ Returns the competition as a list. """
    row = start_row
    col = 0 

    for comp in comp_list:
        print(comp)

    for comp in comp_list:
        # define conditional formatting
        ws.write_row(row, col, comp.to_list())
        
        home_team_cell = xlsxwriter.utility.xl_rowcol_to_cell(row, col+2)
        away_team_cell = xlsxwriter.utility.xl_rowcol_to_cell(row, col+3)

        # conditional format for home team 
        ws.conditional_format(home_team_cell, {'type': 'cell',
                                        'criteria': '<',
                                        'value': comp.away_score,
                                        'format': format_loose})
        ws.conditional_format(home_team_cell, {'type': 'cell',
                                        'criteria': '==',
                                        'value': comp.away_score,
                                        'format': format_tie})
        ws.conditional_format(home_team_cell, {'type': 'cell',
                                        'criteria': '>',
                                        'value': comp.away_score,
                                        'format': format_win})  
        
        # conditional format for away team
        ws.conditional_format(away_team_cell, {'type': 'cell',
                                        'criteria': '<',
                                        'value': comp.home_score,
                                        'format': format_loose})
        ws.conditional_format(away_team_cell, {'type': 'cell',
                                        'criteria': '==',
                                        'value': comp.home_score,
                                        'format': format_tie})
        ws.conditional_format(away_team_cell, {'type': 'cell',
                                        'criteria': '>',
                                        'value': comp.home_score,
                                        'format': format_win})
        
        row += 1



workbook = xlsxwriter.Workbook('report_file.xlsx')
worksheet = workbook.add_worksheet() 


# Formats

# Light red fill with dark red text.
format_loose = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

# Light yellow fill with dark yellow text.
format_tie = workbook.add_format({'bg_color':  '#FFEB9C',
                                 'font_color': '#9C6500'})

# Light green fill with dark green text.
format_win = workbook.add_format({'bg_color':  '#C6EFCE',
                                 'font_color': '#006100'})

worksheet.write('A1', 'Results from 1st match 2024')

line = 2 # start at line 2
for team in teams_for_report:
    worksheet.write_row(line,0, team.to_list())
    line += 1

worksheet.write('A10', 'Ergebnisse')

report_competition(worksheet, 10, comps_for_report)

workbook.close()
