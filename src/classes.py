from typing import List


class Player:
    def __init__(self, name: str):
        self.name = name
        self.power = 0
        self.reg = 0
        self.neg = 0
        self.tempPower = 0
        self.tempReg = 0
        self.tempNeg = 0

    def get_player_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_reg(self):
        return self.reg

    def get_neg(self):
        return self.neg

    def get_tempPower(self):
        return self.tempPower

    def get_tempReg(self):
        return self.tempReg

    def get_tempNeg(self):
        return self.tempNeg

    def add_game_stats(self, p, r, n):
        self.power += p
        self.reg += r
        self.neg += n
        self.tempPower = p
        self.tempReg = r
        self.tempNeg = n

    def reset_temp_stats(self):
        self.tempPower = 0
        self.tempReg = 0
        self.tempNeg = 0


class School:
    def __init__(self, name: str, players: List[str]):
        self.school = name
        self.players = [Player(player) for player in players]
        self.players.sort(
            key=lambda n: n.get_player_name().split()[-1]
        )  # TODO check if this sorts names correctly

    def get_name(self) -> str:
        return self.school

    def get_players(self) -> List[Player]:
        return self.players

    def get_num_players(self) -> int:
        return len(self.players)

    def get_player_strings(self) -> List[str]:
        return [player.get_player_name() for player in self.players]
