import unittest
from openpyxl import load_workbook
from src.sqbs import Matches, Sheet


def load_sheet_by_name(name: str = "ok_example"):
    wb = load_workbook("tests/ucsd_tournament/stats.xlsx")
    return wb[name]


class TestMatches(unittest.TestCase):
    def setUp(self):
        self.match = Matches("tests/ucsd_tournament/stats.xlsx")


class TestSheet(unittest.TestCase):
    pass
