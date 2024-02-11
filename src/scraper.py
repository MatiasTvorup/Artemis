from selenium import webdriver

class Scraper:

    def __init__(self):
        opt = webdriver.FirefoxOptions()
        opt.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opt)


    def scrape(self, url : str) -> str:
        self.driver.get(url)
        page_source = self.driver.page_source
        self.driver.quit()
        return page_source
