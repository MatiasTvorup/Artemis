from scraper import Scraper
from htmlParser import HtmlParser


s = Scraper()
h = HtmlParser()
h.parse(s.scrape("https://danskespil.dk/oddset/sport/783/dart/matches", "EventItemLinkAnchor-0-3-635"))
# f = open("src/test.html", "r")
# h.parse(f.read())