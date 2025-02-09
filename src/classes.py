from typing import List, Tuple


class Player:
    def __init__(self, name: str):
        self.name = name

        self.power = 0
        self.ten = 0
        self.neg = 0

        self.temp_power = 0
        self.temp_ten = 0
        self.temp_neg = 0
        self.temp_tuh = 0

        self.index = -1

    def get_player_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_ten(self):
        return self.ten

    def get_neg(self):
        return self.neg

    def get_temp_stats(self) -> Tuple[int, int, int, int]:
        return self.temp_power, self.temp_ten, self.temp_neg, self.temp_tuh

    def get_index(self):
        assert self.index != -1, f"uninitialized index for {self.get_player_name()}"
        return self.index

    def add_game_stats(self, p, t, n, tuh):
        self.power += p
        self.ten += t
        self.neg += n
        self.temp_power = p
        self.temp_ten = t
        self.temp_neg = n
        self.temp_tuh = tuh

    def reset_temp_stats(self):
        self.temp_power = 0
        self.temp_teg = 0
        self.temp_neg = 0
        self.temp_tuh = 0


class School:
    def __init__(self, name: str, players: List[str]):
        self.school = name.strip()
        self.index = -1

        self.players = [Player(player) for player in players]
        self.players.sort(
            key=lambda n: (
                n.get_player_name().split("(")[0].split()[-1],  # Last name
                " ".join(
                    n.get_player_name().split("(")[0].split()[:-1]
                ),  # First and middle names without suffix
                (
                    n.get_player_name().split("(")[-1].rstrip(")")
                    if "(" in n.get_player_name()
                    else ""
                ),  # Suffix
            )
        )
        for i, player in enumerate(self.players):
            player.index = i
        self.players_dict = {
            player.get_player_name(): player for player in self.players
        }

    def get_name(self) -> str:
        return self.school

    def get_players(self) -> List[Player]:
        return self.players

    def get_num_players(self) -> int:
        return len(self.players)

    def get_player_strings(self) -> List[str]:
        return [player.get_player_name() for player in self.players]

    def get_index(self):
        assert self.index != -1, f"uninitialized index for {self.get_name()}"
        return self.index

    def find_player(self, player_name: str) -> Player:
        return self.players_dict[player_name]
