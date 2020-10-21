from test_locators  import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class user_management(object):
    def __init__(self, driver):
        self.driver = driver
        # user management home page locator defining

        wait = WebDriverWait(driver, 15)
        self.user_management_icon =wait.until(EC.element_to_be_clickable((By.XPATH, locator.user_management_icon)))


class AppRole(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.application_role =wait.until(EC.element_to_be_clickable((By.XPATH, locator.application_role)))




class Add_App_Role(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.Add_AppROle=wait.until(EC.element_to_be_clickable((By.XPATH, locator.add)))



class add_dropdown(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 20)
        self.add_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_field)))



class dropdown_value1(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.value1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_dropdown_value1)))
class dropdown_value2(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.value2 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_dropdown_value2)))

class dropdown_value3(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.value3 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_dropdown_value3)))

class dropdown_closure(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.closure = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_dropdown_closure)))


class details(object):
    def __init__(self, driver):
        self.driver = driver


        wait = WebDriverWait(driver, 10)
        self.name= wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_name)))

class descrp(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.description = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_description)))

class conti(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.contnue = wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_continue)))

class sear(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.search= wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_keyword_search)))






class dropdown_option1(object):

     def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.option1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.permission_option1)))

class dropdown_option2(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.option2 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.permission_option2)))

class dropdown_option3(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.option3= wait.until(EC.element_to_be_clickable((By.XPATH, locator.permission_option3)))

class selc_option1(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.selection1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.permission_option1_selection)))

class selc_option2(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.selection2 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.permission_option2_selection)))

class selc_option3(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.selection3 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.permission_option3_selection)))

class clear_src_field(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.clear_field = wait.until(EC.element_to_be_clickable((By.XPATH, locator.clear_search)))

class add_final(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.finalize= wait.until(EC.element_to_be_clickable((By.XPATH, locator.add_finalize)))



#All Classes are related to a Dashboard automation


class dashboard_search(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.search = wait.until(EC.element_to_be_clickable((By.XPATH, locator.dashboard_search)))

class dashboard_export(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.dashbaord_export= wait.until(EC.element_to_be_clickable((By.XPATH, locator.dashboard_export)))




class pdf_export(object):
    def __init__(self, driver):
        wait = WebDriverWait(driver, 10)
        self.pdf_export= wait.until(EC.element_to_be_clickable((By.XPATH, locator.export_pdf)))



class excel_export(object):
    def __init__(self, driver):

        wait = WebDriverWait(driver, 10)
        self.excel_export = wait.until(EC.element_to_be_clickable((By.XPATH, locator.export_excel)))






class application_dashboard(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.check_dashboard = wait.until(EC.element_to_be_clickable((By.XPATH, locator.check_add_role)))


        wait = WebDriverWait(driver, 10)
        self.filter= wait.until(EC.element_to_be_clickable((By.XPATH, locator.dashboard_filter)))

class pages_selector(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.page_selector= wait.until(EC.element_to_be_clickable((By.XPATH, locator.page_selection)))





class filter_values(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.filter_values = wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_column)))

class column_value(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.column_value= wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_value)))



class filter_operator(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.operator = wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_operator)))


class operator_value(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.operator1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.operator_value1)))

        wait = WebDriverWait(driver, 10)
        self.operator2= wait.until(EC.element_to_be_clickable((By.XPATH, locator.operator_value2)))



class value_field(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.value_field= wait.until(EC.element_to_be_clickable((By.XPATH, locator.value)))




class add_filter_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.add_filter= wait.until(EC.element_to_be_clickable((By.XPATH, locator.filter_add)))




class apply_filter(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.apply_filter= wait.until(EC.element_to_be_clickable((By.XPATH, locator.apply_filter)))

        wait = WebDriverWait(driver, 10)
        self.clear_filter = wait.until(EC.element_to_be_clickable((By.XPATH, locator.clear_filter)))



class appli_dashboard_page_value(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.page_value1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.page_selection_value1)))

        wait = WebDriverWait(driver, 10)
        self.page_value2 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.page_selection_value2)))

        wait = WebDriverWait(driver, 10)
        self.count = wait.until(EC.element_to_be_clickable((By.XPATH, locator.page_count)))

        wait = WebDriverWait(driver, 10)
        self.next_page = wait.until(EC.element_to_be_clickable((By.XPATH, locator.next_page)))

        wait = WebDriverWait(driver, 10)
        self.previous_page= wait.until(EC.element_to_be_clickable((By.XPATH, locator.previous_page)))

        wait = WebDriverWait(driver, 10)
        self.name_column_sorting = wait.until(EC.element_to_be_clickable((By.XPATH, locator.name_sort)))

        wait = WebDriverWait(driver, 10)
        self.description_column_sorting= wait.until(EC.element_to_be_clickable((By.XPATH, locator.description_sort)))

        wait = WebDriverWait(driver, 10)
        self.column_selection= wait.until(EC.element_to_be_clickable((By.XPATH, locator.column_select_deselect)))



class column_selection(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.name_column = wait.until(EC.element_to_be_clickable((By.XPATH, locator.name_column)))

        wait = WebDriverWait(driver, 10)
        self.description_column = wait.until(EC.element_to_be_clickable((By.XPATH, locator.description_column)))

class profile_nav(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.update_profile = wait.until(EC.element_to_be_clickable((By.XPATH, locator.edit_profile)))

class profile_view(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.view_profile = wait.until(EC.element_to_be_clickable((By.XPATH, locator.profile_view)))



class contnue_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 15)
        self.continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, locator.edit_profile_continue)))

class save_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.save_button = wait.until(EC.element_to_be_clickable((By.XPATH, locator.edit_profile_save_button)))

class previ_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.previous_button = wait.until(EC.element_to_be_clickable((By.XPATH, locator.previous_button)))

class bck_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 15)
        self.back_button = wait.until(EC.element_to_be_clickable((By.XPATH, locator.back_button)))


class more_option(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 15)
        self.more_option = wait.until(EC.element_to_be_clickable((By.XPATH, locator.more_option)))


class deactivate_button(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 15)
        self.deactivate_button= wait.until(EC.element_to_be_clickable((By.XPATH, locator.deactivate_profile)))

class deactivate_notification(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.deactivate_notification = wait.until(EC.element_to_be_clickable((By.XPATH, locator.deactivate_notification)))

class restore_profile(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 15)
        self.restore_button = wait.until(EC.element_to_be_clickable((By.XPATH, locator.restore_profile)))


class delete_profile(object):
     def __init__(self, driver):
         self.driver = driver

         wait = WebDriverWait(driver, 10)
         self.delete_button= wait.until(EC.element_to_be_clickable((By.XPATH, locator.delete_profile)))



class footer_navigation(object):
    def __init__(self, driver):
        self.driver = driver

        wait = WebDriverWait(driver, 10)
        self.footer_page2= wait.until(EC.element_to_be_clickable((By.XPATH, locator.footer_page2)))

        wait = WebDriverWait(driver, 10)
        self.footer_page1 = wait.until(EC.element_to_be_clickable((By.XPATH, locator.footer_page1)))

        wait = WebDriverWait(driver, 10)
        self.footer_next_page = wait.until(EC.element_to_be_clickable((By.XPATH, locator.footer_next_page)))

        wait = WebDriverWait(driver, 10)
        self.footer_previous_page = wait.until(EC.element_to_be_clickable((By.XPATH, locator.footer_previous_page)))









# self.application_user = driver.find_element(By.XPATH,locator.application_user)
# self.user_group = driver.find_element(By.XPATH,locator.user_group)
# self.settings= driver.find_element(By.XPATH,locator.settings)
# self.scorecard_parameter = driver.find_element(By.XPATH,locator.scorecard_parameters)
# self.scorecard = driver.find_element(By.XPATH,locator.scorecard)
