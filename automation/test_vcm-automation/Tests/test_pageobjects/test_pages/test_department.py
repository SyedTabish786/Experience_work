from test_locators import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC








class department(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.department = wait.until(EC.element_to_be_clickable((By.XPATH, locator.department)))

class add_department(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.add_depart = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_depart)))


class ADD_department_name(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_name = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_depart_name)))

class ADD_head_department(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.head_depart = wait.until(EC.element_to_be_clickable((By.XPATH, locator.depart_head)))


class ADD_department_head_value(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.head_value= wait.until(EC.element_to_be_clickable((By.XPATH, locator.head_drop_down)))


class ADD_department_finalize(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.add_finalize = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_depart_finalize)))

class depart_dashboard(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_dashboard_search= wait.until(EC.element_to_be_clickable((By.XPATH, locator.depart_dashboard_search)))

class depart_dashboard_ex(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_dashbaord_export = wait.until(EC.element_to_be_clickable((By.XPATH, locator.dashboard_export)))


class depart_pdf_export(object):
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.depart_pdf_export = wait.until(EC.element_to_be_clickable((By.XPATH, locator.export_pdf)))

class depart_excel_export(object):
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 10)
        self.depart_excel_export = wait.until(EC.element_to_be_clickable((By.XPATH, locator.export_excel)))


class depart_dashboard_view(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.filter = wait.until(EC.element_to_be_clickable((By.XPATH, locator.dashboard_filter)))


class department_filter_values(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_colm_values= wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_column)))

class department_filter_operator(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_operator = wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_operator)))

class depart_column_value(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.column_value = wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_value)))

class depart_operator_value(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.operator1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.operator_value1)))

class depart_operator2_value2(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.operator2 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.operator_value2)))

class depart_value_field(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_value_field= wait.until(EC.element_to_be_clickable((By.XPATH, locator.value)))


class depart_add_filter_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.add_filter= wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_add)))

class depart_apply_filter(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.depart_apply_filter = wait.until(EC.element_to_be_clickable((By.XPATH, locator.apply_filter)))

        wait = WebDriverWait(driver, 10)
        self.depart_clear_filter= wait.until(EC.element_to_be_clickable((By.XPATH, locator.clear_filter)))




