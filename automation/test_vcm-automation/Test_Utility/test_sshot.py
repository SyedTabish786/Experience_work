from selenium import webdriver


class ss(object):

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, path):
        directory = ("/Users/tabish/Documents/automation/vcm-automation/screenshots")
        self.driver.get_screenshot_as_file(directory + path)
