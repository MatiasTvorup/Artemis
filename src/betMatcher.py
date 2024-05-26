from bet import Bet

class Match:
    b1 = {}
    b2 = {}

    def __init__(self, bet1 : Bet, bet2 : Bet):
        self.b1 = bet1
        self.b2 = bet2

class BetMatcher:

    def MatchBets(self, betList1 : list, betList2 : list) -> list[Match]:
        matchList = []
        
        for b1 in betList1:
            for b2 in betList2:
                if self.isMatch(b1,b2):
                    matchList.append(Match(b1, b2))
                    del b1
                    del b2
                    break
            
            

        return matchList

    def isMatch(self, bet1 : Bet, bet2 : Bet) -> bool:
        return (bet1.team1Name == bet2.team1Name and bet1.team2Name == bet2.team2Name) or (bet1.team1Name == bet2.team2Name and bet1.team2Name == bet2.team1Name)