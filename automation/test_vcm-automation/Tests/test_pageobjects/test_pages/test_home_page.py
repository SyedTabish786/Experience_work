from test_locators import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# class Home(object):
#     def __init__(self, driver):
#         self.driver = driver

        # login page locator defining
        # self.logo = driver.find_element(By.XPATH, locator.logo)
        # self.login_dropdown = driver.find_element(By.XPATH, locator.login_drop)

# def getlogo(self):
    #     return self.logo




class Home(object):

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait (driver, 10)
        self.drop_menu = wait.until(EC.element_to_be_clickable((By.XPATH, locator.login_drop)))


