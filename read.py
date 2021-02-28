#!/usr/bin/env python
import xlrd
class Matches:
    schools = []
    wb = ''
    def __init__(self, loc):
        self.wb = loc
        sheet = self.wb.sheet_by_name("Rosters")
        for i in range(sheet.nrows - 1):
            sName = sheet.cell_value(i + 1, 0)
            players = []
            for j in range(sheet.ncols - 1):
                playerName = sheet.cell_value(i + 1, j + 1)
                if playerName:
                    players.append(playerName)
            self.schools.append(School(sName, players))

    def get_schools(self):
        return self.schools
    
    def collect_sheet(self, sheet, sheetNumber):
        #https://www.qbwiki.com/wiki/SQBS_data_file info from here
        #ID, team1 index, team2 index, team1 score, team2 score, TUH, Rnd#
        #team1 bonuses heard, team1 bonus pts, team 2 bonuses heard, team2 bonus pts
        #getting team names
        team1 = sheet.cell_value(0, 2)
        team2 = sheet.cell_value(0, 12)
        #getting team indexes
        team1Index = 0
        team2Index = 0
        count = 0
        for x in self.schools:
            if x.get_name() == team1:
                team1Index = count
            if x.get_name() == team2:
                team2Index = count
            count += 1
        #getting team scores
        team1Score = int(sheet.cell_value(36, 1))
        team2Score = int(sheet.cell_value(36, 14))
        #getting tuh
        tuh = 1
        for i in range(6):
            num = sheet.cell_value(31, 2 + i)
            if (num > tuh):
                tuh = int(num)
        #round number
        rndNumber = int(sheet.cell_value(2, 23))
        #bonuses heard/allocating points to individuals
        team1BonusesHeard = 0
        team2BonusesHeard = 0
        for i in range(self.schools[team1Index].get_number()):
            player = self.schools[team1Index].get_individuals()[i]
            p = sheet.cell_value(32, 2 + i)
            r = sheet.cell_value(33, 2 + i)
            n = sheet.cell_value(34, 2 + i)
            player.add_game_stats(p, r, n)
            team1BonusesHeard += int(p + r)
        for i in range(self.schools[team2Index].get_number()):
            player = self.schools[team2Index].get_individuals()[i]
            p = sheet.cell_value(32, 12 + i)
            r = sheet.cell_value(33, 12 + i)
            n = sheet.cell_value(34, 12 + i)
            player.add_game_stats(p, r, n)
            team2BonusesHeard += int(p + r)
        #bonus points
        team1BonusPoints = int(sheet.cell_value(31, 8))
        team2BonusPoints = int(sheet.cell_value(31, 18))
        #overtime, random stuff, random stuff, forfeit, lightning round, lightning round all 0
        stuff = str(0)
        #playerCounts
        playersString = ''
        for i in range(16):
            playerNum = 0
            if i % 2 == 0:
                school = self.schools[team1Index]
                playerNum = int(i / 2)
            else:
                playerNum = int((i + 1) / 2 - 1)
                school = self.schools[team2Index]
            if playerNum + 1 > school.get_number():
                    playersString = playersString + '-1\n'
                    for i in range(6):
                        playersString = playersString + stuff + '\n'
            else:
                p = school.get_individuals()[int(playerNum)]
                if i % 2 == 0:
                    playerGP = sheet.cell_value(31, int(2 + playerNum)) / tuh
                else: 
                    playerGP = sheet.cell_value(31, int(12 + playerNum)) / tuh
                if playerGP == 0 or playerGP == 1:
                    playerGP = int(playerGP)
                playerP = int(p.get_tempPower())
                playerR = int(p.get_tempReg())
                playerN = int(p.get_tempNeg())
                points = int(playerP * 15 + playerR * 10 - playerN * 5)
                playersString = playersString + str(playerNum) + '\n' + str(playerGP) + '\n'
                playersString = playersString + str(playerP) + '\n' + str(playerR) + '\n' + str(playerN) + '\n' + stuff + '\n' + str(points) + '\n'
                p.reset_temp_stats()
        #string compilation
        sheetOutput = str(sheetNumber) + '\n'
        sheetOutput = sheetOutput + str(team1Index) + '\n' + str(team2Index) + '\n'
        sheetOutput = sheetOutput + str(team1Score) + '\n' + str(team2Score) + '\n'
        sheetOutput = sheetOutput + str(tuh) + '\n' + str(rndNumber) + '\n'
        sheetOutput = sheetOutput + str(team1BonusesHeard) + '\n' + str(team1BonusPoints) + '\n'
        sheetOutput = sheetOutput + str(team2BonusesHeard) + '\n' + str(team2BonusPoints) + '\n'
        for i in range(6):
            sheetOutput = sheetOutput + stuff + '\n'
        sheetOutput = sheetOutput + playersString
        return sheetOutput

    def create_sqbs_string(self):
        #number of teams
        output = str(len(self.schools)) + '\n'
        #each team (1 + people) + school name + one line for each player
        for s in self.schools:
            output = output + str(s.get_number() + 1) + '\n' + s.get_name() + '\n'
            for i in s.get_individuals():
                output = output + i.get_indiv() + '\n'
        #number of matches total
        totalSheets = wb.nsheets - 1
        output = output + str(totalSheets) + '\n'
        #getting info from sheet
        sheetNames = wb.sheet_names()
        counter = 1
        for i in sheetNames:
            if i != 'Rosters':
                output = output + self.collect_sheet(wb.sheet_by_name(i), counter)
            counter += 1
        #ppb tracking?, automatic?, tracking p/n (3), lightning?, tuh heard, etc. note divisions is here and can be manually changed
        output = output + '1\n1\n3\n0\n1\n2\n254\n1\n1\n1\n1\n1\n1\n1\n0\n0\n4\n'
        #name of tournament, ftp settings
        output = output + 'Arizona Quizbowl Association Monthly Invitational\n\n\n\n\n0\n'
        output = output + '_rounds.html\n_standings.html\n_individuals.html\n_games.html\n_teamdetail.html\n_playerdetail.html\n_statkey.html\n'
        #division number probably do this manually
        output = output + '0\n' + str(len(self.schools))+ '\n'
        for i in range(len(self.schools)):
            output = output + '-1\n'
        #Unsure what these values are, but they make it work
        output = output + '15\n-1\n-1\n-1\n-1\n-1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n'
        #point values
        output = output + '15\n10\n-5\n0\n0\n' + str(len(self.schools)) + '\n'
        #0 for teams since we don't use exhibition teams
        for i in range(len(self.schools)):
            output = output + '0\n'
        return output
        
class School:
    def __init__(self, sName, iNames):
        self.school = sName
        self.individuals = []
        count = 0
        for x in iNames:
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

if __name__ == '__main__':
    #C:\\Users\\denis\\code\\python\\QBStats\\stats.xlsx
    print('Input File Location: ')
    path = input()
    wb = xlrd.open_workbook(path)
    obj = Matches(wb)
    with open('sqbs.sqbs', 'w') as writer:
        sqbs = obj.create_sqbs_string()
        writer.write(sqbs)