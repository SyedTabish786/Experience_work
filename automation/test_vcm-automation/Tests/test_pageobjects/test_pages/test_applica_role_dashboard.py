from test_locators import locator
from selenium.webdriver.common.by import By



class dashboard_search(object):
    def __init__(self, driver):
        self.driver = driver
        self.search = driver.find_element(By.XPATH, locator.dashboard_search)
