from scraper import Scraper
from htmlParser import OddsetParser
from htmlParser import NordicBetParser
from betMatcher import BetMatcher
from betMatcher import Match

s = Scraper()
op = OddsetParser()
np = NordicBetParser()


odd = op.parse(s.scrape("https://danskespil.dk/oddset/sport/783/dart/matches", "marketOutcomes"))
nordic = np.parse(s.scrape("https://www.nordicbet.dk/betting/dart/international", "obg-event-row-event-container"))

bm = BetMatcher()
list = bm.MatchBets(nordic, odd)

for m in list:
    print(m.b1)
    print(m.b2)
if(list.count() == 0):
    print("LIst is empty")
