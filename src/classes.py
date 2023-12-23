class School:
    def __init__(self, sName, iNames):
        self.school = sName
        self.individuals = []
        count = 0
        for _ in iNames:
            self.individuals.append(Individual(iNames[count]))
            count = count + 1

    def get_name(self):
        return self.school

    def get_individuals(self):
        return self.individuals

    def get_number(self):
        return len(self.individuals)

    def get_individual_strings(self):
        players = []
        count = 0
        for x in self.individuals:
            players.append(x.get_indiv())
            count += 1
        return players


class Individual:
    def __init__(self, iName):
        self.indiv = iName
        self.power = 0
        self.reg = 0
        self.neg = 0
        self.tempPower = 0
        self.tempReg = 0
        self.tempNeg = 0

    def get_indiv(self):
        return self.indiv

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
