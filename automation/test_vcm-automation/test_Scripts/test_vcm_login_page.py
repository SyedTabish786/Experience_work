import unittest
from time import sleep
from test_home_page import Home
from test_signup_page import login
from test_EnvironmentSetup import EnvironmentSetup
from selenium.webdriver.common.keys import Keys




class vcm_login_page(EnvironmentSetup):
    def test_loginflow(self):
        driver = self.driver
        self.driver.get("http://157.230.179.140/login?redirect=%2F")
        expected_title = "Value Chain Management System"

        try:
            if driver.title == expected_title:
                print("Home Page loaded successfully")
                self.assertEqual(driver.title, expected_title)
        except Exception as a:
            print(" Home Page Title Assertion Failed Due To : " + str(a))
            self.driver.set_page_load_timeout(10)
            sleep(10)

        home = Home(driver)

        try:
            if home.drop_menu.text == "login":
                self.assertEqual(home.drop_menu.text, "login")
                print("Login DropDown Assertion is Passed")
                home.drop_menu.click()
        except Exception as b:
            print("Login DropDown Assertion Failed Due TO :" + str(b))

        log_in = login(driver)
        try:
            if (log_in.user_name.get_attribute("id") == "username"):
                print("User Name Field Assertion is Passed")
                self.assertEqual(log_in.user_name.get_attribute("id"), "username")
                log_in.user_name.send_keys("admin.super")
        except Exception as c:
            print("User Name Field Assertion Failed Due To : " + str(c))
        try:
            if (log_in.password.get_attribute("id") == "password"):
                print("Password Field Assertion is Passed")
                self.assertEqual(log_in.password.get_attribute("id"), "password")
                log_in.password.send_keys("conor")
        except Exception as d:
            print("Password Field Assertion Failed Due To : " + str(d))

        try:
            if (log_in.submit_button.text == "Login"):
                print("Login Button Assertion is Passed")
                self.assertEqual(log_in.submit_button.text, "Login")
                log_in.submit_button.click()
        except Exception as e:
            print("Login Button Assertion is Failed Due To:" + str(e))


if __name__ == '__main__':
    unittest.main()
