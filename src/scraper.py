from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Scraper:

    def __init__(self):
        opt = webdriver.FirefoxOptions()
        opt.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opt)


    def scrape(self, url : str, pageLoadedClass : str) -> str:
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, pageLoadedClass)))
        page_source = self.driver.page_source
        # self.driver.quit()
        return page_source
