

class Bet:
    team1Name = ""
    team2Name = ""
    team1WinOdds = 0
    team2WinOdds = 0


    def __init__(self, team1 : str, team2 : str, t1Odds : float, t2Odds : float):
        self.team1Name = team1
        self.team2Name = team2
        self.team1WinOdds = t1Odds
        self.team2WinOdds = t2Odds

    def __str__(self):
        return self.team1Name + ": " + str(self.team1WinOdds) + "\n" + self.team2Name + ": " + str(self.team2WinOdds)
        

    def isInitialized(self):
        return self.team1Name != "" and self.team2Name != "" and self.team1WinOdds != 0 and self.team2WinOdds != 0 