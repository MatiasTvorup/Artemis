from selenium import webdriver

class Scraper:
    __url__ = ""

    def __init__(self, url : str):
        self.__url__ = url

    def setUrl(self, url : str):
        self.__url__ = url

    def scrape(self) -> str:
        print("SCRAPING " + self.__url__)


        opt = webdriver.FirefoxOptions()
        opt.add_argument("--headless")
        driver = webdriver.Firefox(options=opt)
        driver.get(self.__url__)
        page_source = driver.page_source
        driver.quit()
        return page_source
