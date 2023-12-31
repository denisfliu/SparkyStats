import unittest
import os
from src.sqbs import Matches, Sheet, get_sheet_config
from tests.const import MatchConst


def path_joiner(path: str):
    return os.path.join(*path.split("/"))


class TestMatches(unittest.TestCase):
    def setUp(self):
        config_path = path_joiner("tests/ucsd_test_config.yaml")
        self.match = Matches(
            path_joiner("tests/ucsd_tournament"), config_path=config_path
        )

    def test_init(self):
        self.assertEqual(
            MatchConst.expected_schools,
            [school.get_name() for school in self.match.schools],
            "Alphabetical schools",
        )
        self.assertEqual(
            self.match.schools[-1].get_player_strings(),
            MatchConst.john_players,
            "John team alphabetical",
        )
        self.assertEqual(
            self.match.schools[2].get_player_strings(),
            MatchConst.bcfd_players,
            "BCFD team alphabetical",
        )
        self.assertEqual(len(self.match.sheets), 4, "there should be four sheets")

    def test_private_functions(self):
        self.assertEqual(self.match._Matches__number_of_teams(), "8")
        self.assertEqual(
            self.match._Matches__all_team_information(), MatchConst.team_string
        )
        self.assertEqual(self.match._Matches__number_of_matches(), "4")
        self.assertEqual(self.match._Matches__tournament_name(), "UCSD_Test")

    def test_compile_sqbs_string(self):
        self.match.compile_sqbs_string()


if __name__ == "__main__":
    unittest.main()
