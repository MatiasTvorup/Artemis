

class Bet:
    team1Name = ""
    team2Name = ""
    team1WinOdds = 0
    team2WinOdds = 0

    startTime = ""
    source = ""


    def __init__(self, team1 : str, team2 : str, t1Odds : float, t2Odds : float):
        self.team1Name = team1
        self.team2Name = team2
        self.team1WinOdds = t1Odds
        self.team2WinOdds = t2Odds

    def __eq__(self, other):
        return self.team1Name == other.team1Name and self.team2Name == other.team2Name

    def print(self):
        print("---")
        print(self.team1Name + ": " + self.team1WinOdds)
        print(self.team2Name + ": " + self.team2WinOdds)
        if self.startTime != "":
            print("Start time: " + self.startTime)
        if self.source != "":
            print("Source: " + self.source)
        else:
            print("Source: Unkown.")
        print("---")
        

    def isInitialized(self):
        return self.team1Name != "" and self.team2Name != "" and self.team1WinOdds != 0 and self.team2WinOdds != 0 