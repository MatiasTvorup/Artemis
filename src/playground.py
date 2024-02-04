from selenium import webdriver

driver = webdriver.Firefox()# Open a web page
driver.get("https://python.org")
print(driver.title)
driver.quit()