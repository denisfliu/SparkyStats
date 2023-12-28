import os
from typing import List
from openpyxl import load_workbook

from src.classes import School, Player


class Matches:
    """
    https://www.qbwiki.com/wiki/SQBS_data_file
    """

    def __init__(self, tournament_directory: str):
        self.files = [
            file for file in os.listdir(tournament_directory) if file.endswith(".xlsx")
        ]
        roster_sheet = os.path.join(tournament_directory, "roster.xlsx")

        assert roster_sheet in self.files, "roster.xlsx required"
        self.files.remove(roster_sheet)

        self.schools: List[School]
        self.init_roster(roster_sheet)

    def init_roster(self, roster_sheet):
        roster_wb = load_workbook(roster_sheet)
        assert len(roster_wb.sheetnames) == 1, "roster sheet should have one sheet"

        ws = roster_wb.active
        for row in ws.iter_rows():
            school = ""
            players = []
            for i, name in enumerate(row):
                if i == 0:
                    school = name
                else:
                    players.append(name)
            self.schools.append(School(name=school, players=players))
        self.schools.sort(key=lambda school: school.get_name())

    def number_of_teams(self) -> str:
        return str(len(self.schools))

    def all_team_information(self) -> str:
        """
        For each team:
            1 plus number of players
            Team Name
            Each player name on a separate line
        """

        def team_string(school: School) -> str:
            return (
                [school.get_num_players() + 1, school.get_name()]
                .extend(school.get_player_strings())
                .join("\n")
            )

        return [team_string(school) for school in self.schools].join("\n")

    def number_of_matches(self) -> str:
        count = 0
        for file in self.files():
            wb = load_workbook(file)
            count += len(wb.sheetnames)
        return str(count)

    ### Match strings
    def matches_strings(self) -> str:
        def parse_sheet(ws) -> str:
            raise NotImplemented

        workbooks = [load_workbook(file) for file in self.files]
        sheet_strings = [parse_sheet(wb[sheet]) for wb in workbooks for sheet in wb]
        return sheet_strings.join("\n")
