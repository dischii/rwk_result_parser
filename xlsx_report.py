""" This module creates a report file in xlsx format. """ 

import xlsxwriter
import xlsxwriter.worksheet

# --------------------------------------------------------------
# testdata


# from competition import Competition
# from team import Team

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

# --------------------------------------------------------------

class XLSXReport:
    """ This class creates a report in xlsx format. """
    def __init__(self, filename: str = 'report.xlsx', header: str = 'Results from 1st match 2024'):
        """ Initializes the report with the given filename. """
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()
        self.last_row = 0

        print(f"{self.workbook.filename} has been created.")

        # Light red fill with dark red text.
        self.format_loose = self.workbook.add_format({'bg_color':   '#FFC7CE',
                                    'font_color': '#9C0006'})

        # Light yellow fill with dark yellow text.
        self.format_tie = self.workbook.add_format({'bg_color':  '#FFEB9C',
                                        'font_color': '#9C6500'})

        # Light green fill with dark green text.
        self.format_win = self.workbook.add_format({'bg_color':  '#C6EFCE',
                                        'font_color': '#006100'})

        self.worksheet.write('A1', header)
        self.last_row += 2 # 1 empty row

    def report_competition(self, comp_list: list):
        """ Returns the competition as a list. """
        row = self.last_row
        col = 0

        # write header
        self.worksheet.write(row, col, 'Ergebnisse')
        row += 1

        # write data and conditional formatting
        for comp in comp_list:
            # define conditional formatting
            self.worksheet.write_row(row, col, comp.to_list())

            home_team_cell = xlsxwriter.utility.xl_rowcol_to_cell(row, col+2)
            away_team_cell = xlsxwriter.utility.xl_rowcol_to_cell(row, col+3)

            # conditional format for home team
            self.worksheet.conditional_format(home_team_cell, {'type': 'cell',
                                            'criteria': '<',
                                            'value': comp.away_score,
                                            'format': self.format_loose})
            self.worksheet.conditional_format(home_team_cell, {'type': 'cell',
                                            'criteria': '==',
                                            'value': comp.away_score,
                                            'format': self.format_tie})
            self.worksheet.conditional_format(home_team_cell, {'type': 'cell',
                                            'criteria': '>',
                                            'value': comp.away_score,
                                            'format': self.format_win})  

            # conditional format for away team
            self.worksheet.conditional_format(away_team_cell, {'type': 'cell',
                                            'criteria': '<',
                                            'value': comp.home_score,
                                            'format': self.format_loose})
            self.worksheet.conditional_format(away_team_cell, {'type': 'cell',
                                            'criteria': '==',
                                            'value': comp.home_score,
                                            'format': self.format_tie})
            self.worksheet.conditional_format(away_team_cell, {'type': 'cell',
                                            'criteria': '>',
                                            'value': comp.home_score,
                                            'format': self.format_win})

            row += 1

        self.last_row = row


    def report_team(self, team_list: list):
        """ Returns the competition as a list. """
        row = self.last_row
        col = 0

        # write header
        self.worksheet.write(row, col, 'Teams')
        row += 1

        for team in team_list:
            self.worksheet.write_row(row, col, team.to_list())
            row += 1

        self.last_row = row


    def close(self):
        """ Closes the workbook. """
        self.worksheet.autofit()
        self.workbook.close()
