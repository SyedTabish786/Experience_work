import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class EnvironmentSetup(unittest.TestCase):

#setUP contains the browser setup attributes
    def setUp(self):
            #self.driver = webdriver.Chrome("/Users/tabish/Documents/automation/vcm-automation/venv/bin/chromedriver")
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            self.driver = webdriver.Chrome(options=options)


            print ("Run Started at :"+str(datetime.datetime.now()))
            print("Chrome Environment Set Up")
            print("------------------------------------------------------------------")
            self.driver.implicitly_wait(20)

            self.driver.maximize_window()

#tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if (self.driver != None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()