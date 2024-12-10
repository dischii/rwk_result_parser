""" This module creates a report file in xlsx format. """ 

import xlsxwriter

import xlsxwriter.worksheet
from competition import Competition
from team import Team

# testdata - TODO: replace test data with acutal data from results.py
comp1 = Competition("home", "away", "1:2")
comp2 = Competition("home2", "away2", "2:1")
comp3 = Competition("home3", "away3", "3:3")
comp4 = Competition("home4", "away4", "4:5")
comps = [comp1, comp2, comp3, comp4]

team = Team("league", "name", 1, "points", "cut")
    

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

worksheet.write('A1', 'Hello')
        
worksheet.write_row(2,0, team.to_list())

worksheet.write('A5', 'Ergebnisse')

report_competition(worksheet, 5, comps)

workbook.close()
