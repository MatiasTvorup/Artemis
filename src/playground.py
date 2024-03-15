from scraper import Scraper
from htmlParser import OddsetParser
from htmlParser import NordicBetParser


s = Scraper()
op = OddsetParser()
np = NordicBetParser()

np.parse(s.scrape("https://www.nordicbet.dk/betting/dart/international", "obg-event-info-participant-name"))
# op.parse(s.scrape("https://danskespil.dk/oddset/sport/783/dart/matches", "EventItemLinkAnchor-0-3-635"))