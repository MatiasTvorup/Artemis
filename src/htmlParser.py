from bs4 import BeautifulSoup
import re
from bet import Bet

class OddsetParser:

    def __init__(self):
        pass

    def parse(self, html : str) -> list[Bet]:
        betList = []
        
        soup = BeautifulSoup(html, "html.parser")
        games = soup.find_all('div', class_= re.compile('eventListItemContent'))
        
        for game in games:
            soup = BeautifulSoup(str(game), "html.parser")
            
            teams = soup.find_all('div', class_=re.compile('eventCardTeamName'))
            if len(teams) != 2:
                continue
            
            odds = soup.find_all('span', class_=re.compile('outcomePriceCommon'))
            if len(odds) != 2:
                continue
            
            b = Bet(teams[0].contents[0], teams[1].contents[0], odds[0].contents[0], odds[1].contents[0])

            time = soup.find_all('span', class_=re.compile('eventCardEventStartTimeText'))
            if len(time) == 1:
                b.startTime = time[0].contents[0]
            
            if b.isInitialized():
                betList.append(b)

        for b in betList:
            b.print()
        return betList

class NordicBetParser:
    def parse(self, html : str) -> list[Bet]:
        betList = []

        soup = BeautifulSoup(html, "html.parser")
        games = soup.find_all('div', class_= re.compile('obg-event-row-event-container'))

        for game in games:
            soup = BeautifulSoup(str(game), "html.parser")

            teams = soup.find_all('span', class_=re.compile('obg-event-info-participant-name'))
            if len(teams) != 2:
                continue
            
            
            oddsContainers = soup.find_all('div', class_=re.compile('obg-selection-base-odds'))
            if len(oddsContainers) != 2:
                continue

            odds = []
            for container in oddsContainers:
                oddSoup = BeautifulSoup(str(container), "html.parser")
                tempOdds = oddSoup.find_all('span', class_=re.compile('ng-star-inserted'))
                for odd in tempOdds:
                    odds.append(odd)

            if len(odds) != 2:
                continue

            b = Bet(teams[0].contents[0], teams[1].contents[0], odds[0].contents[0], odds[1].contents[0])
            if b.isInitialized():
                betList.append(b)

        return betList