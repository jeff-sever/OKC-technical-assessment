import math

class Team:
    Corner3M = 0
    Corner3A = 0
    NonCorner3M = 0
    NonCorner3A = 0
    TwoPtM = 0
    TwoPtA = 0
    SDCorner3 = 0.0
    SDNonCorner3 = 0.0
    SDTwoPt = 0.0
    eFGPercent2Pt = 0.0
    eFGPercentC3 = 0.0
    eFGPercentNC3 = 0.0

    def Corner3Make(self):
        self.Corner3M += 1
        self.Corner3A += 1

    def NonCorner3Make(self):
        self.NonCorner3M += 1
        self.NonCorner3A += 1

    def TwoPointMake(self):
        self.TwoPtM += 1
        self.TwoPtA += 1

    def ShotDistribution(self):
        FGA = self.Corner3A + self.NonCorner3A + self.TwoPtA
        self.SDTwoPt = self.TwoPtA / FGA
        self.SDCorner3 = self.Corner3A / FGA
        self.SDNonCorner3 = self.NonCorner3A / FGA

    def efgPercent(self):
        self.eFGPercent2Pt = self.TwoPtM / self.TwoPtA
        self.eFGPercentNC3 = (self.NonCorner3M + (0.5 * self.NonCorner3M)) / self.NonCorner3A
        self.eFGPercentC3 = (self.Corner3M + (0.5 * self.Corner3M)) / self.Corner3A

    def roundNumbers(self):
        self.eFGPercent2Pt = round(self.eFGPercent2Pt, 3)
        self.eFGPercentNC3 = round(self.eFGPercentNC3, 3)
        self.eFGPercentC3 = round(self.eFGPercentC3, 3)
        self.SDTwoPt = round(self.SDTwoPt, 3)
        self.SDCorner3 = round(self.SDCorner3, 3)
        self.SDNonCorner3 = round(self.SDNonCorner3, 3)


if __name__ == '__main__':
    shotData = open("shots_data.csv")
    shotData.readline()
    TeamA = Team()
    TeamB = Team()
    for line in shotData:
        fields = line.split(",")
        for word in fields:
            word.replace("'", "")
        fields[3] = fields[3].replace("\n", "")
        if fields[0] == "Team A":
            if fields[3] == "1":
                if abs(float(fields[1])) > 22:
                    if abs(float(fields[2])) <= 7.8:
                        TeamA.Corner3Make()
                elif math.sqrt((float(fields[1])) ** 2 + (float(fields[2])) ** 2) > 23.75:
                    TeamA.NonCorner3Make()
                else:
                    TeamA.TwoPointMake()
            else:
                if abs(float(fields[1])) > 22:
                    if abs(float(fields[2])) <= 7.8:
                        TeamA.Corner3A += 1
                elif math.sqrt((float(fields[1])) ** 2 + (float(fields[2])) ** 2) > 23.75:
                    TeamA.NonCorner3A += 1
                else:
                    TeamA.TwoPtA += 1
        elif fields[0] == "Team B":
            if fields[3] == "1":
                if abs(float(fields[1])) > 22:
                    if abs(float(fields[2])) <= 7.8:
                        TeamB.Corner3Make()
                elif math.sqrt((float(fields[1])) ** 2 + (float(fields[2])) ** 2) > 23.75:
                    TeamB.NonCorner3Make()
                else:
                    TeamB.TwoPointMake()
            else:
                if abs(float(fields[1])) > 22:
                    if abs(float(fields[2])) <= 7.8:
                        TeamB.Corner3A += 1
                elif math.sqrt((float(fields[1])) ** 2 + (float(fields[2])) ** 2) > 23.75:
                    TeamB.NonCorner3A += 1
                else:
                    TeamB.TwoPtA += 1

    TeamA.efgPercent()
    TeamB.efgPercent()
    TeamA.ShotDistribution()
    TeamB.ShotDistribution()
    TeamA.roundNumbers()
    TeamB.roundNumbers()

    print("eFG for Team A: ")
    print("2pt Zone: " + str(TeamA.eFGPercent2Pt))
    print("NC3 Zone: " + str(TeamA.eFGPercentNC3))
    print("C3 Zone: " + str(TeamA.eFGPercentC3))
    print("Shot Distribution for Team A: ")
    print("2 Point Shots: " + str(TeamA.SDTwoPt))
    print("Non Corner 3-Point Shots: " + str(TeamA.SDNonCorner3))
    print("Corner 3-Point Shots: " + str(TeamA.SDCorner3) + "\n")

    print("eFG for Team B: ")
    print("2pt Zone: " + str(TeamB.eFGPercent2Pt))
    print("NC3 Zone: " + str(TeamB.eFGPercentNC3))
    print("C3 Zone: " + str(TeamB.eFGPercentC3))
    print("Shot Distribution for Team B: ")
    print("2 Point Shots: " + str(TeamB.SDTwoPt))
    print("Non Corner 3-Point Shots: " + str(TeamB.SDNonCorner3))
    print("Corner 3-Point Shots: " + str(TeamB.SDCorner3))

