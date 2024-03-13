from bs4 import BeautifulSoup
import re
from bet import Bet

class HtmlParser:

    def __init__(self):
        pass

    def parse(self, html : str) -> list[Bet]:
        betList = list[Bet]
        
        soup = BeautifulSoup(html, "html.parser")
        games = soup.find_all('div', class_= re.compile('eventListItemContent'))
        
        if(len(games) == 0):
            return betList
        
        for game in games:
            soup = BeautifulSoup(str(game), "html.parser")
            teams = soup.find_all('div', class_=re.compile('eventCardTeamName'))
            if len(teams) != 2:
                continue
            odds = soup.find_all('span', class_=re.compile('outcomePriceCommon'))
            if len(odds) != 2:
                continue

            betList.append(Bet(teams[0].contents[0], teams[1].contents[0], odds[0].contents[0], odds[1].contents[0]))

        return betList
