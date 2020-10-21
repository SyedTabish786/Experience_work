import unittest
from time import sleep

from allure_commons.types import AttachmentType
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from test_locators import locator
from test_management_page import user_management
from test_management_page import AppRole
import allure


from test_management_page import Add_App_Role
from test_management_page import add_dropdown
from test_management_page import dropdown_value1
from test_management_page import dropdown_value2
from test_management_page import dropdown_value3
from test_management_page import dropdown_closure
from test_management_page import details
from test_management_page import descrp
from test_management_page import conti
from test_management_page import sear
from test_management_page import clear_src_field
from test_management_page import dropdown_option1
from test_management_page import selc_option1
from test_management_page import dropdown_option2
from test_management_page import selc_option2
from test_management_page import dropdown_option3
from test_management_page import selc_option3
from test_management_page import add_final
from test_management_page import dashboard_search
from test_management_page import dashboard_export
from test_management_page import pdf_export
from test_management_page import excel_export

from test_management_page import application_dashboard
from test_management_page import pages_selector
from test_management_page import filter_values
from test_management_page import filter_operator
from test_management_page import column_value
from test_management_page import operator_value
from test_management_page import value_field
from test_management_page import add_filter_button
from test_management_page import apply_filter
from test_management_page import column_selection
from test_management_page import profile_nav
from test_management_page import contnue_button
from test_management_page import save_button
from test_management_page import bck_button
from test_management_page import previ_button
from test_management_page import profile_view
from test_management_page import more_option
from test_management_page import deactivate_button
from test_management_page import deactivate_notification
from test_management_page import restore_profile
from test_management_page import delete_profile
from test_management_page import footer_navigation
from test_management_page import appli_dashboard_page_value
from test_department import department
from test_department import add_department
from test_department import ADD_department_name
from test_department import ADD_head_department
from test_department import ADD_department_head_value
from test_department import ADD_department_finalize
from test_department import depart_dashboard
from test_department import depart_dashboard_ex
from test_department import depart_pdf_export
from test_department import depart_excel_export
from test_department import depart_dashboard_view
from test_department import department_filter_values
from test_department import depart_column_value
from test_department import depart_operator_value
from test_department import department_filter_operator
from test_department import depart_value_field
from test_department import depart_add_filter_button
from test_department import depart_apply_filter
from test_department import depart_operator2_value2

from test_EnvironmentSetup import EnvironmentSetup
from test_home_page import Home
from test_signup_page import login


class vcm_user_managementPage(EnvironmentSetup):
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_management_flow(self):
        driver = self.driver
        driver.implicitly_wait(50)
        # self.driver.get("http://167.172.129.57/login?redirect=%2F")
        self.driver.get("http://157.230.179.140/login?redirect=%2F")

        expected_title = "Value Chain Management System"

        try:
            if driver.title == expected_title:
                print("Home Page loaded successfully")
                self.assertEqual(driver.title, expected_title)
        except Exception as a:
            allure.attach(self.driver.get_screenshot_as_png(), name="Test login screen title assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print(" Home Page Title Assertion Failed Due To : " + str(a))
            self.driver.set_page_load_timeout(10)

        home = Home(driver)

        try:
            if home.drop_menu.text == "login":
                self.assertEqual(home.drop_menu.text, "login")
                print("Login DropDown Assertion is Passed")
                home.drop_menu.click()
        except Exception as b:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Dropdown Box  Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Login DropDown Assertion Failed Due TO :" + str(b))


        log_in = login(driver)
        try:
            if (log_in.user_name.get_attribute("id") == "username"):
                print("User Name Field Assertion is Passed")
                self.assertEqual(log_in.user_name.get_attribute("id"), "username")
                log_in.user_name.send_keys("admin.super")
        except Exception as c:
            allure.attach(self.driver.get_screenshot_as_png(), name="UserName Text Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("User Name Field Assertion Failed Due To : " + str(c))
        try:
            if (log_in.password.get_attribute("id") == "password"):
                print("Password Field Assertion is Passed")
                self.assertEqual(log_in.password.get_attribute("id"), "password")
                log_in.password.send_keys("conor")
        except Exception as d:
            allure.attach(self.driver.get_screenshot_as_png(), name="Password Text Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Password Field Assertion Failed Due To : " + str(d))

        try:
            if (log_in.submit_button.text == "Login"):
                print("Login Button Assertion is Passed")
                self.assertEqual(log_in.submit_button.text, "Login")
                log_in.submit_button.click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Button  Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Login Button Assertion is Failed Due To:" + str(e))

        user = user_management(driver)
        try:
            if (user.user_management_icon.text == "supervisor_account"):
                print("User Management Icon Assertion is Passed")
                self.assertEqual(user.user_management_icon.text, "supervisor_account")
                user.user_management_icon.click()



        except Exception as f:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="User Management Module Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("User Management Icon Assertion Failed Due To :" + str(f))
        log = AppRole(driver)
        try:
            if (log.application_role.text == "Application Role"):
                print("Application Role  Assertion is Passed")
                self.assertEqual(log.application_role.text, "Application Role")
                log.application_role.click()
        except Exception as g:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="User Management Application Role Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Assertion is Failed Due To : " + str(g))

        role = Add_App_Role(driver)
        try:
            if (role.Add_AppROle.text == "Add New\nadd"):
                print("Add Application-Role Assertion is passed")
                self.assertEqual(role.Add_AppROle.text, "Add New\nadd")
                role.Add_AppROle.click()


        except Exception as h:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="User Management Application Role Add Role Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Add Application-Role Assertion is Failed Due TO : " + str(h))

        dropdown = add_dropdown(driver)
        try:
            if (dropdown.add_dropdown.get_attribute("id") == "moduleIds"):
                print("Application Module Selection DropDown Assertion is Passed")
                self.assertEqual(dropdown.add_dropdown.get_attribute("id"), "moduleIds")
                dropdown.add_dropdown.click()

        except Exception as i:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Module Selection DropDown Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Module Selection DropDown Assertion is Failed Due To : " + str(i))
        value1 = dropdown_value1(driver)
        try:
            if (value1.value1.text == "Vendor Compliance"):
                print("Selection of Value one from Dropdown list Assertion is Passed")
                self.assertEqual(value1.value1.text, "Vendor Compliance")
                value1.value1.click()

        except Exception as j:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Selection of Value one from Dropdown list Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Selection of Value one from Dropdown list Assertion is Failed Due To : " + str(j))

        value2 = dropdown_value2(driver)
        try:
            if (value2.value2.text == "Meeting Management"):
                print("Selection of Value Two from Dropdown list Assertion is Passed")
                self.assertEqual(value2.value2.text, "Meeting Management")
                value2.value2.click()

        except Exception as k:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Selection of Value Two from Dropdown list Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Selection of Value Two from Dropdown list Assertion is Failed Due To :" + str(k))
        value3 = dropdown_value3(driver)
        try:
            if (value3.value3.text == "Change Management"):
                print("Selection of Value Three from Dropdown list Assertion is Passed")
                self.assertEqual(value3.value3.text, "Change Management")
                value3.value3.click()

        except Exception as l:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Selection of Value Three from Dropdown list Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Selection of Value Three from Dropdown list Assertion is Failed Due To :" + str(l))

        closure = dropdown_closure(driver)
        try:
            if (closure.closure.get_attribute("class") == "v-input__append-inner"):
                print("Dropdown list Closure Assertion is Passed ")
                self.assertEqual(closure.closure.get_attribute("class"), "v-input__append-inner")
                closure.closure.click()

        except Exception as m:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Dropdown List Closure  Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Dropdown list Closure Assertion is Failed Due To :  " + str(m))
        data = details(driver)
        try:
            if (data.name.get_attribute("id") == "name"):
                print("Add Name Field Assertion is Passed")
                self.assertEqual(data.name.get_attribute("id"), "name")
                data.name.send_keys("Automation User")

        except Exception as n:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Add Name Field  Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Add Name Field Assertion is Failed Due To : " + str(n))

        desc = descrp(driver)
        try:
            if (desc.description.get_attribute("id") == "description"):
                print("Add Description Field Assertion is Passed")
                self.assertEqual(desc.description.get_attribute("id"), "description")
                desc.description.send_keys("Tester")
        except Exception as o:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Add Description Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Add Description Field Assertion is Failed Due To : " + str(o))
        contin = conti(driver)
        try:
            if (contin.contnue.text == "Continue\narrow_forward"):
                print("Add Continue Assertion is Passed")
                self.assertEqual(contin.contnue.text, "Continue\narrow_forward")
                contin.contnue.click()

        except Exception as o:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Add Continue Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Add Continue Assertion is Failed Due To : " + str(o))
        srch = sear(driver)
        try:
            if (srch.search.get_attribute("id") == "search"):
                print("Add Keyword Search Field Assertion is Passed")
                self.assertEqual(srch.search.get_attribute("id"), "search")
                srch.search.click()
                srch.search.send_keys("Compliance")

        except Exception as p:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Add Keyword Search Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Add Keyword Search Field Assertion is Failed Due To : " + str(p))

        option1 = dropdown_option1(driver)
        try:
            if (option1.option1.text == "Vendor Compliance"):
                print("Vendor Compliance Option Assertion is Passed")
                self.assertEqual(option1.option1.text, "Vendor Compliance")
                option1.option1.click()

        except Exception as q:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Vendor Compliance Option Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Vendor Compliance Option Assertion is Failed Due To : " + str(q))
        select_option1 = selc_option1(driver)
        try:
            if (select_option1.selection1.text == "check_box_outline_blank"):
                print("Vendor Compliance Option Selection Assertion is Passed")
                self.assertEqual(select_option1.selection1.text, "check_box_outline_blank")
                select_option1.selection1.click()

        except Exception as r:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Vendor Compliance Option Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Vendor Compliance Option Selection Assertion is Failed Due To : " + str(r))

        clear = clear_src_field(driver)
        try:
            if (clear.clear_field.get_attribute("class") == "v-input__icon v-input__icon--clear"):
                print("Keyword Search Field Clear Assertion is Passed")
                self.assertEqual(clear.clear_field.get_attribute("class"), "v-input__icon v-input__icon--clear")
                clear.clear_field.click()

        except Exception as s:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Keyword Search Field Clear Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Keyword Search Field Clear Assertion is Failed Due To: " + str(s))
        option2 = dropdown_option2(driver)
        srch.search.click()
        srch.search.send_keys("Meeting")
        try:

            if (option2.option2.text == "Meeting Management"):
                print("Meeting Management Option Selection Assertion is Passed")
                self.assertEqual(option2.option2.text, "Meeting Management")
                option2.option2.click()

        except Exception as t:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Meeting Management Option Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Meeting Management Option Selection Assertion is Failed Due To : " + str(t))

        select_option2 = selc_option2(driver)
        try:
            if (select_option2.selection2.text == "check_box_outline_blank"):
                print("Meeting Managemeent Selection Assertion is Passed")
                self.assertEqual(select_option2.selection2.text, "check_box_outline_blank")
                select_option2.selection2.click()

        except Exception as u:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Meeting Management Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Meeting Management Selection Assertion is Failed Due To :" + str(u))
        try:
            clear.clear_field.click()
        except (StaleElementReferenceException)as e:
            self.clear_field = driver.find_element(By.XPATH, locator.clear_search)
            self.clear_field.click()
            print(str(e))

        option3 = dropdown_option3(driver)
        try:

            srch.search.click()

            srch.search.send_keys("Chang")
        except (StaleElementReferenceException) as e:
            self.search = self.driver.find_element(By.XPATH, locator.add_keyword_search)
            self.search.click()
            self.search.send_keys("Change")
            print(str(e))
        try:
            if (option3.option3.text == "keyboard_arrow_down"):
                print("Change Management Option Assertion is Passed")
                self.assertEqual(option3.option3.text, "keyboard_arrow_down")
                option3.option3.click()

        except Exception as v:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Change Management Option Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Change Management Option Assertion is Failed Due To : " + str(v))

        selet_option3 = selc_option3(driver)
        try:
            if (selet_option3.selection3.text == "check_box_outline_blank"):
                print("Change Management Option Selection Assertion is Passed")
                self.assertEqual(selet_option3.selection3.text, "check_box_outline_blank")
                selet_option3.selection3.click()

        except Exception as x:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Change Management Option Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Change Management Option Selection Assertion is Failed Due To : " + str(x))

        add_final_role = add_final(driver)
        try:
            if (add_final_role.finalize.text == "Add"):
                print("Application Add Role Final Assertion is Passed")
                self.assertEqual(add_final_role.finalize.text, "Add")
                add_final_role.finalize.click()

        except Exception as y:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Add Role Final Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Add Role Final Assertion is Failed Due To : " + str(y))

        search = dashboard_search(driver)
        try:
            if (search.search.get_attribute("id") == "input-430"):
                print("Application Role Dashboard Search Field Assertion is Passed")
                self.assertEqual(search.search.get_attribute("id"), "input-430")
                search.search.click()

                search.search.send_keys("Automation")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Search Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashboard Search Field Assertion is Failed Due To : " + str(e))
        export = dashboard_export(driver)
        try:
            if (export.dashbaord_export.text == "Export\nsave_alt"):
                print("Application Role Dashboard Export Button Assertion is Passed")
                self.assertEqual(export.dashbaord_export.text, "Export\nsave_alt")
                export.dashbaord_export.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Export Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashboard Export Button Assertion is Failed Due To : " + str(e))

        pdf = pdf_export(driver)
        try:
            if (pdf.pdf_export.text == "PDF"):
                print("Application Role Dashboard PDF Export Button Assertion is Passed")
                self.assertEqual(pdf.pdf_export.text, "PDF")
                pdf.pdf_export.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard PDF Export Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashbaord PDF Export Button Assertion is Failed Due To : " + str(e))

        export.dashbaord_export.click()

        excel = excel_export(driver)
        try:

            if (excel.excel_export.text == "Excel"):
                print("Application Role Dashboard EXCEL Export Button Assertion is Passed")
                self.assertEqual(excel.excel_export.text, "Excel")
                excel.excel_export.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard EXCEL Export Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashbaord EXCEL Export Button Assertion is Failed Due To : " + str(e))

        dashboard = application_dashboard(driver)
        try:
            if (dashboard.filter.text == "Filter\ntune"):
                print("Application Role Dashboard Filter Assertion is passed")
                self.assertEqual(dashboard.filter.text, "Filter\ntune")
                dashboard.filter.click()

        except Exception as a:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Filter Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Filter Assertion is Failed Due To : " + str(a))
        d_value = filter_values(driver)
        try:
            if (d_value.filter_values.get_attribute("id") == "selectedColumn"):
                print("Application Role Dashboard Filter Column Value Sekection Assertion is Passed")
                self.assertEqual(d_value.filter_values.get_attribute("id"), "selectedColumn")
                d_value.filter_values.click()

        except Exception as b:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Filter Column Value Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Filter Column Value Selection Assertion is Failed Due To : " + str(b))
        col_value = column_value(driver)
        try:
            if (col_value.column_value.text == "Name"):
                print("Application Role Dashboard Filter Column Value Selection Assertion is Passed")
                self.assertEqual(col_value.column_value.text, "Name")
                col_value.column_value.click()
        except Exception as c:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard FIlter Column Value Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Filter Column Value Selection Assertion is Failed Due To :" + str(c))

        filter_opr = filter_operator(driver)
        try:
            if (filter_opr.operator.get_attribute("id") == "selectedOperator"):
                print("Application Role Dashboard Filter Operator Field Assertion is Passed")
                self.assertEqual(filter_opr.operator.get_attribute("id"), "selectedOperator")
                filter_opr.operator.click()

        except Exception as c:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Filter Operator Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Filter Operator Field Assertion is Failed Due To : " + str(c))
        opr = operator_value(driver)
        try:
            if (opr.operator1.text == "Equals"):
                print("Application Role Dashboard Filter Operator Value one Assertion is Passed")
                self.assertEqual(opr.operator1.text, "Equals")
                opr.operator1.click()


        except Exception as d:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Filter Operator Value Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Filter Operator Value Assertion is Failed Due To : " + str(d))
        val = value_field(driver)
        try:
            if (val.value_field.get_attribute("id") == "value"):
                print("Application Role Dashboard Filter Value Field Assertion is Passed")
                self.assertEqual(val.value_field.get_attribute("id"), "value")
                val.value_field.send_keys("Automation User")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Filter Value Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Filter Value Field Assertion is Failed Due To : " + str(e))

        add = add_filter_button(driver)
        try:
            if (add.add_filter.text == "Add\nadd"):
                print("Application Role  Add Filter Button Assertion is Passed")
                self.assertEqual(add.add_filter.text, "Add\nadd")
                add.add_filter.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Add Filter Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Add Filter Button Assertion is Failed Due To : " + str(e))

        apply = apply_filter(driver)
        try:
            if (apply.apply_filter.text == "Apply Filter\ntune"):
                print("Application Role Dashboard Apply Filter Button Assertion is Passed ")
                self.assertEqual(apply.apply_filter.text, "Apply Filter\ntune")
                apply.apply_filter.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Apply Filter Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Apply Filter Button Assertion is Failed Due To : " + str(e))

        dashboard.filter.click()

        try:
            d_value.filter_values.click()

        except (StaleElementReferenceException) as e:
            self.filter_values = driver.find_element(By.XPATH, locator.filter_column)
            self.filter_values.click()
            print(str(e))
        try:
            col_value.column_value.click()
        except (StaleElementReferenceException) as a:

            self.column_value = driver.find_element(By.XPATH, locator.filter_value)
        finally:
            self.column_value.click()

        try:
            filter_opr.operator.click()
        except (StaleElementReferenceException) as b:
            self.operator = driver.find_element(By.XPATH, locator.filter_operator)
        finally:
            self.operator.click()

        try:

            opr.operator2.click()
        except (StaleElementReferenceException) as c:
            try:
                self.operator2 = driver.find_element(By.XPATH, locator.operator_value2)
                if (self.operator2.text == "Contains"):
                    print("Application Role Dashboard Filter Operator Two Value Assertion is Passed")
                    self.assertEqual(self.operator2.text, "Contains")
            finally:
                self.operator2.click()

            # else:
            #     print("Application Role Dashboard Filter Operator Two Value Assertion is Failed Due To : " + str(c))
        try:
            val.value_field.send_keys("Automation")
        except (StaleElementReferenceException) as d:
            self.val = driver.find_element(By.XPATH, locator.value)
            self.val.send_keys("Automation")

        try:
            add.add_filter.click()
        except (StaleElementReferenceException) as e:
            self.add_filter = driver.find_element(By.XPATH, locator.filter_add)
            self.add_filter.click()

        try:
            apply.apply_filter.click()
        except (StaleElementReferenceException) as f:
            self.apply_filter = driver.find_element(By.XPATH, locator.apply_filter)
            self.apply_filter.click()

        try:
            if (apply.clear_filter.text == "Clear All Filter"):
                print("Application Role Dashboard Clear All Filter Button Assertion is Passed")
                self.assertEqual(apply.clear_filter.text, "Clear All Filter")
                apply.clear_filter.click()

        except Exception as g:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Clear All Filter Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Clear All Filter Button Assertion is Failed Due To : " + str(g))

        dashboard = pages_selector(driver)
        try:
            if (dashboard.page_selector.get_attribute("class") == "v-icon notranslate mdi mdi-menu-down theme--light"):
                print("Application Role Dashboard Page Selection Assertion is Passed")
                self.assertEqual(dashboard.page_selector.get_attribute("class"),
                                 "v-icon notranslate mdi mdi-menu-down theme--light")
                dashboard.page_selector.click()


        except Exception as h:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Page Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Page Selection Assertion is Failed Due To : " + str(h))

        selector = appli_dashboard_page_value(driver)
        try:

            if (selector.page_value1.text == "50"):
                print("Application Role Dashboard Page value Selection Assertion is Passed")
                self.assertEqual(selector.page_value1.text, "50")
                selector.page_value1.click()


        except Exception as i:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Page Value Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Page value Selection Assertion is Failed Due To : " + str(i))
        try:
            dashboard.page_selector.click()

            if (selector.page_value2.text == "25"):
                print("Application Role Dashboard Page value Selection Assertion is Passed")
                self.assertEqual(selector.page_value2.text, "25")
                selector.page_value2.click()


        except Exception as j:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Page value Selection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Page value Selection Assertion is Failed Due To : " + str(j))

        try:
            if (selector.count.text == "1-25 of 29"):
                print("Application Role Dashboard Viewed Record Per Page Assertion is Passed")
                self.assertEqual(selector.count.text, "1-25 of 29")
        except Exception as k:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Viewed Record Per Page Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Viewed Record Per Page Assertion is Failed Due To : " + str(k))
        try:

            if (selector.next_page.text == "arrow_right"):
                print("Application Role Dashboard Next Page Button Assertion is Passed")
                self.assertEqual(selector.next_page.text, "arrow_right")
                selector.next_page.click()

        except Exception as l:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Next Page Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Next Page Button Assertion is Failed Due To : " + str(l))
        try:
            if (selector.count.text == "26-29 of 29"):
                print("Application Role Dashboard Next Page Viewed Record Per Page Assertion is Passed")
                self.assertEqual(selector.count.text, "26-29 of 29")
        except Exception as m:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Next Page Viewed Record Per Page Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Next Page Viewed Record Per Page Assertion is Failed Due To : " + str(m))
        try:
            if (selector.previous_page.text == "arrow_left"):
                print("Application Role Dashboard Previous Page Button Assertion is Passed")
                self.assertEqual(selector.previous_page.text, "arrow_left")
                selector.previous_page.click()

        except Exception as n:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Previous Page Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Previous Page Button Assertion is Failed Due To : " + str(n))
        try:
            if (selector.count.text == "1-25 of 29"):
                print("Application Role Dashboard Previous Page Viewed Record Per Page Assertion is Passed")
                self.assertEqual(selector.count.text, "1-25 of 29")

        except Exception as o:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Previous Page Viewed Record Per Page Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Previous Page Viewed Record Per Page Assertion is Failed Due To : " + str(
                o))

        try:
            if (selector.name_column_sorting.text == "sort"):
                print("Application Role Dashboard Name Column Sorting Assertion is Passed")
                self.assertEqual(selector.name_column_sorting.text, "sort")
                selector.name_column_sorting.click()
                selector.name_column_sorting.click()

        except Exception  as p:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Name Column Sorting Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Name Column Sorting Assertion is Failed Due To : " + str(p))
        try:
            if (selector.description_column_sorting.text == "sort"):
                print("Application Role Dashboard Description Column Sorting Assertion is Passed")
                self.assertEqual(selector.description_column_sorting.text, "sort")
                selector.description_column_sorting.click()

                selector.description_column_sorting.click()
        except Exception as q:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Description Column Sorting Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Description Column Sorting Assertion is Failed Due To : " + str(q))

        try:
            if (selector.column_selection.is_displayed() == True):
                print("Application Role Dashboard Column Selection Dropdown Assertion is Passed")
                self.assertEqual(selector.column_selection.is_displayed(), True)
                selector.column_selection.click()

        except Exception as r:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Column Selection Dropdown Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Column Selection Dropdown Assertion is Passed" + str(r))
        colmn = column_selection(driver)
        try:

            if (colmn.name_column.text == "Name"):
                print("Application Role Dashboard Name Column Deselection Assertion is Passed")
                self.assertEqual(colmn.name_column.text, "Name")
                colmn.name_column.click()

        except Exception as t:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Name Column Deselection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Name Column Deselection Assertion is Failed Due To : " + str(t))

        try:
            if (colmn.description_column.text == "Description"):
                print("Application Role Dashboard Description Column Deselection Assertion is Passed")
                self.assertEqual(colmn.description_column.text, "Description")
                colmn.description_column.click()

                colmn.name_column.click()

                colmn.description_column.click()

        except Exception as r:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Description Column Deselection Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard Description Column Deselection Assertion is Failed Due To : " + str(r))

        profile = profile_nav(driver)
        try:
            if (profile.update_profile.text == "edit"):
                print("Application Role Dashboard Update Profile Button Assertion is Passed")
                self.assertEqual(profile.update_profile.text, "edit")
                self.driver.refresh()

                try:
                    profile.update_profile.click()
                except (StaleElementReferenceException) as e:
                    allure.attach(self.driver.get_screenshot_as_png(),
                                  name="Application Role Dashboard Update Profile Button Assertion is Failed",
                                  attachment_type=AttachmentType.PNG)

                    self.update_profile = driver.find_element(By.XPATH, locator.edit_profile)
                    if (self.update_profile.text == "edit"):
                        print("Application Role Dashboard Update Profile Button Assertion is Passed")
                        self.assertEqual(self.update_profile.text, "edit")
                        self.update_profile.click()

        except Exception as m:
            print("Application Role Dashboard Update Profile Button Assertion is Failed Due To : " + str(m))

        button = contnue_button(driver)

        try:
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            if (button.continue_button.text == "Continue\narrow_forward"):
                print("Application Role Dashbaord Update Profile Continue Button Assertion is Passed")
                self.assertEqual(button.continue_button.text, "Continue\narrow_forward")
                button.continue_button.click()



        except Exception as n:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Update Profile Continue Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashbaord Update Profile Continue Button Assertion is Failed Due To : " + str(n))
        selet_option3 = selc_option3(driver)
        try:
            selet_option3.selection3.click()

        except (StaleElementReferenceException) as e:
            self.selection3 = driver.find_element(By.XPATH, locator.permission_option3_selection)
            self.selection3.click()

            self.selection3.click()

        save_btn = save_button(driver)

        try:
            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            if (save_btn.save_button.text == "Save"):
                print("Application Role Dashbaord Update Profile Save Button Assertion is Passed")
                self.assertEqual(save_btn.save_button.text, "Save")
                save_btn.save_button.click()

        except Exception as o:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Update Profile Continue Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashbaord Update Profile Continue Button Assertion is Failed Due To : " + str(o))
        prof = profile_view(driver)
        try:
            if (prof.view_profile.text == "remove_red_eye"):
                print("Application Role Dashboard View Profile Button Assertion is Passed")
                self.assertEqual(prof.view_profile.text, "remove_red_eye")
                prof.view_profile.click()
        except Exception as p:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard View Profile Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Application Role Dashboard View Profile Button Assertion is Failed Due To : " + str(p))

        try:

            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            button.continue_button.click()
        except (StaleElementReferenceException) as e:

            self.continue_button = driver.find_element(By.XPATH, locator.edit_profile_continue)
            self.continue_button.click()

        prv_button = previ_button(driver)

        try:
            driver.execute_script("window.scrollTo(0,11000)")
            prv_button.previous_button.click()


        except (StaleElementReferenceException) as e:

            self.previous_button = driver.find_element(By.XPATH, locator.previous_button)

            if (self.previous_button.text == "arrow_back\nPrevious"):

                print("Application Role Dashboard View Profile Previous Button Assertion is Passed")
                self.assertEqual(self.previous_button.text, "arrow_back\nPrevious")
                self.previous_button.click()

            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Application Role Dashboard View Profile Previous Button Assertion is Failed",
                              attachment_type=AttachmentType.PNG)

                print("Application Role Dashboard View Profile Previous Button Assertion is Failed Due To : " + str(e))

        bak_button = bck_button(driver)

        try:
            # driver.execute_script("window.scrollTo(0,500)")
            bak_button.back_button.click()
        except (StaleElementReferenceException) as e:

            self.back_button = driver.find_element(By.XPATH, locator.back_button)
            if (self.back_button.back_button.text == "Back"):

                print("Application Role Dashboard View Profile Back Button Assertion is Passed")
                self.assertEqual(self.back_button.back_button.text, "Back")
                self.back_button.back_button.click()


            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Application Role Dashboard View Profile Back Button Assertion is Failed",
                              attachment_type=AttachmentType.PNG)

                print("Application Role Dashboard View Profile Back Button Assertion is Failed Due To : ")
        more = more_option(driver)
        try:
            if (more.more_option.text == "more_vert"):
                print("Application Role Dashboard Profile More Options Assertion is Passed")
                self.assertEqual(more.more_option.text, "more_vert")
                more.more_option.click()


        except Exception as s:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard View Profile More Options Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashboard Profile More Options Assertion is Failed Due To : " + str(s))

        deactivate = deactivate_button(driver)
        try:
            if (deactivate.deactivate_button.text == "Deactivate"):
                print("Application Role Dashbaord Profile More Options Deactivate Button Assertion is Passed")
                self.assertEqual(deactivate.deactivate_button.text, "Deactivate")
                deactivate.deactivate_button.click()

        except Exception as t:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Profile More Options Deactivate Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print(
                "Application Role Dashbaord Profile More Options Deactivate Button Assertion is Failed Due To : " + str(
                    t))
        notification = deactivate_notification(driver)
        try:
            if (notification.deactivate_notification.text == "Deactivate"):
                print("Application Role Dashbaord Profile More Options Deactivate Confirmation Assertion is Passed")
                self.assertEqual(notification.deactivate_notification.text, "Deactivate")
                notification.deactivate_notification.click()
                sleep(5)

        except Exception as u:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Profile More Options Deactivate Confirmation Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print(
                "Application Role Dashbaord Profile More Options Deactivate Confirmation Assertion is Failed Due To : " + str(
                    u))

        try:

            more.more_option.click()
        except (StaleElementReferenceException) as e:
            self.more_option = self.driver.find_element(By.XPATH, locator.more_option)
            self.more_option.click()
            sleep(5)

        restore = restore_profile(driver)
        try:
            if (restore.restore_button.text == "Restore"):
                print("Application Role Dashboard Profile More Option Restore Button Assertion is Passed")
                self.assertEqual(restore.restore_button.text, "Restore")
                restore.restore_button.click()
                sleep(5)

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Profile More Option Restore Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashboard Profile More Option Restore Button Assertion is Failed Due To " + str(e))
        # delete = delete_profile(driver)
        # try:
        #     if (delete.delete_button.text == "Delete"):
        #         print("Application Role Dashboard Profile More Option Delete Button Assertion is Passed")
        #         self.assertEqual(delete.delete_button.text, "Delete")
        #         delete.delete_button.click()
        #
        # except Exception as e:
        #     allure.attach(self.driver.get_screenshot_as_png(),
        #                   name="Application Role Dashboard Profile More Option Delete Button Assertion is Failed",
        #                   attachment_type=AttachmentType.PNG)
        #     print("Application Role Dashboard Profile More Option Delete Button Assertion is Failed Due To : " + str(e))
        footer = footer_navigation(driver)

        try:
            # driver.execute_script("window.scrollTo(0,2500)")
            if (footer.footer_page2.text == "2"):
                print("Application Role Dashboard Footer Navigation Page 2 Button Assertion is Passed")
                self.assertEqual(footer.footer_page2.text, "2")
                footer.footer_page2.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Footer Navigation Page 2 Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashboard Footer Navigation Page 2 Button Assertion is Failed Due To : " + str(e))

        try:
            if (footer.footer_previous_page.get_attribute(
                    "class") == "v-icon notranslate mdi mdi-chevron-left theme--light"):
                print("Application Role Dashboard Footer Navigation Previous Page Button Assertion is Passed")
                self.assertEqual(footer.footer_previous_page.get_attribute("class"),
                                 "v-icon notranslate mdi mdi-chevron-left theme--light")
                footer.footer_previous_page.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Footer Navigation Previous Page Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print(
                "Application Role Dashboard Footer Navigation Previous Page Button Assertion is Failed Due To : " + str(
                    e))

        try:
            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            if (footer.footer_next_page.get_attribute(
                    "class") == "v-icon notranslate mdi mdi-chevron-right theme--light"):
                print("Application Role Dashbaord Footer Navigation Next Page Button Assertion is Passed")
                self.assertEqual(footer.footer_next_page.get_attribute("class"),
                                 "v-icon notranslate mdi mdi-chevron-right theme--light")
                footer.footer_next_page.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Footer Navigation Next Page Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashbaord Footer Navigation Next Page Button Assertion is Failed Due To : " + str(
                e))

        try:
            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            if (footer.footer_page1.text == "1"):
                print("Application Role Dashboard Footer Navigation Page 1 Button Assertion is Passed")
                self.assertEqual(footer.footer_page1.text, "1")
                footer.footer_page1.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Application Role Dashboard Footer Navigation Page 1 Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Application Role Dashboard Footer Navigation Page 1 Button Assertion is Failed Due To : " + str(e))
        depart = department(driver)
        try:
            if (depart.department.text == "Department"):
                print("User Management Department Button Assertion is Passed")
                self.assertEqual(depart.department.text, "Department")
                depart.department.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="User Management Department Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("User Management Department Button Assertion is Failed Due To : " + str(e))
        add = add_department(driver)
        try:
            if (add.add_depart.text == "Add New\nadd"):
                print("User Management Department Add New Button Assertion is Passed")
                self.assertEqual(add.add_depart.text, "Add New\nadd")
                add.add_depart.click()


        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="User Management Department Add New Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("User Management Department Add New Button Assertion is Failed Due To : " + str(e))
        name = ADD_department_name(driver)
        try:
            if (name.depart_name.get_attribute("id") == "name"):
                print("Department Dashbaord Add New Department Name field Assertion is Passed")
                self.assertEqual(name.depart_name.get_attribute("id"), "name")
                name.depart_name.send_keys("QA-Department")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Add New Depart Text Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Add New Department field Assertion is Failed Due To : " + str(e))
        head = ADD_head_department(driver)
        try:
            if (head.head_depart.get_attribute("id") == "applicationUserId"):
                print("Department Dashbaord Add Head of Department Field Assertion is Passed")
                self.assertEqual(head.head_depart.get_attribute("id"), "applicationUserId")
                head.head_depart.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Add Head Of Department Text Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashbaord Add Head of Department Field Assertion is Failed Due To : " + str(e))
        head_value = ADD_department_head_value(driver)
        try:
            if (head_value.head_value.text == "Admin Super"):
                print("Department Dashbaord Add Head Dropdown List Assertion is Passed")
                self.assertEqual(head_value.head_value.text, "Admin Super")
                head_value.head_value.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Add Head Dropdown List Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashbaord Add Head Dropdown List Assertion is Failed Due To : " + str(e))

        add_finalize = ADD_department_finalize(driver)
        try:
            if (add_finalize.add_finalize.text == "Add"):
                print("Department Dashboard Add Department Button Assertion is Passed")
                self.assertEqual(add_finalize.add_finalize.text, "Add")
                add_finalize.add_finalize.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Add Department Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Add Department Button Assertion is Failed Due To : " + str(e))
        depart_search = depart_dashboard(driver)
        try:
            if (depart_search.depart_dashboard_search.get_attribute("id") == "input-430"):
                print("Department Dashboard Search Field Assertion is Passed")
                self.assertEqual(depart_search.depart_dashboard_search.get_attribute("id"), "input-430")
                depart_search.depart_dashboard_search.click()

                depart_search.depart_dashboard_search.send_keys("QA-Department")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Search Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Search Field Assertion is Failed Due To : " + str(e))
        depart_exprt = depart_dashboard_ex(driver)
        try:
            if (depart_exprt.depart_dashbaord_export.text == "Export\nsave_alt"):
                print("Department Dashboard Export Button Assertion is Passed")
                self.assertEqual(depart_exprt.depart_dashbaord_export.text, "Export\nsave_alt")
                depart_exprt.depart_dashbaord_export.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Export Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)

            print("Department Dashboard Export Button Assertion is Failed Due To : " + str(e))

        pdf = depart_pdf_export(driver)
        try:
            if (pdf.depart_pdf_export.text == "PDF"):
                print("Department Dashboard PDF Export Button Assertion is Passed")
                self.assertEqual(pdf.depart_pdf_export.text, "PDF")
                pdf.depart_pdf_export.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard PDF Export Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashbaord PDF Export Button Assertion is Failed Due To : " + str(e))

        depart_exprt.depart_dashbaord_export.click()

        depart_excel = depart_excel_export(driver)
        try:

            if (depart_excel.depart_excel_export.text == "Excel"):
                print("Department Dashboard EXCEL Export Button Assertion is Passed")
                self.assertEqual(depart_excel.depart_excel_export.text, "Excel")
                depart_excel.depart_excel_export.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard EXCEL Export Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashbaord EXCEL Export Button Assertion is Failed Due To : " + str(e))
        depart_view = depart_dashboard_view(driver)
        try:
            if (depart_view.filter.text == "Filter\ntune"):
                print("Department Dashboard Filter Assertion is passed")
                self.assertEqual(depart_view.filter.text, "Filter\ntune")
                depart_view.filter.click()

        except Exception as a:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Filter Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Filter Assertion is Failed Due To : " + str(a))
        depart_value = department_filter_values(driver)
        try:
            if (depart_value.depart_colm_values.get_attribute("id") == "selectedColumn"):
                print("Department Dashboard Filter Column Value Sekection Assertion is Passed")
                self.assertEqual(depart_value.depart_colm_values.get_attribute("id"), "selectedColumn")
                depart_value.depart_colm_values.click()

        except Exception as b:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Filter Column Value SelectionAssertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Filter Column Value Selection Assertion is Failed Due To : " + str(b))
        depart_col = depart_column_value(driver)
        try:
            if (depart_col.column_value.text == "Name"):
                print("Department Dashboard Filter Column Value Selection From Dropdown List is Passed")
                depart_col.column_value.click()

        except Exception as c:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Filter Column Value Selection From Dropdown List Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print(
                "Department Dashboard Filter Column Value Selection From Dropdown List is Failed Due To : " + str(
                    c))
        depart_oprt = department_filter_operator(driver)
        try:
            if (depart_oprt.depart_operator.get_attribute("id") == "selectedOperator"):
                print("Department Dashboard Filter Operation Field Assertion is Passed")
                self.assertEqual(depart_oprt.depart_operator.get_attribute("id"), "selectedOperator")
                depart_oprt.depart_operator.click()

        except Exception as c:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Filter Operator Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Filter Operator Field Assertion is Failed Due To : " + str(c))
        depart_opr = depart_operator_value(driver)
        try:
            if (depart_opr.operator1.text == "Equals"):
                print("Department Dashboard Filter Operator Value one Assertion is Passed")
                self.assertEqual(depart_opr.operator1.text, "Equals")
                depart_opr.operator1.click()

        except Exception as d:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Filter Operator Value Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Filter Operator Value Assertion is Failed Due To : " + str(d))
        depart_val = depart_value_field(driver)
        try:
            if (depart_val.depart_value_field.get_attribute("id") == "value"):
                print("Department Dashboard Filter Value Field Assertion is Passed")
                self.assertEqual(depart_val.depart_value_field.get_attribute("id"), "value")
                depart_val.depart_value_field.send_keys("QA-Department")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Filter Value Field Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Filter Value Field Assertion is Failed Due To : " + str(e))
        depart_add_filter = depart_add_filter_button(driver)
        try:
            if (depart_add_filter.add_filter.text == "Add\nadd"):
                print("Department Dashboard Add Filter Button Assertion is Passed")
                self.assertEqual(depart_add_filter.add_filter.text, "Add\nadd")
                depart_add_filter.add_filter.click()


        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Add Filter Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Add Filter Button Assertion is Failed Due To : " + str(e))
        depart_apply = depart_apply_filter(driver)
        try:
            if (depart_apply.depart_apply_filter.text == "Apply Filter\ntune"):
                print("Department Dashboard Apply Filter Button Assertion is Passed ")
                self.assertEqual(depart_apply.depart_apply_filter.text, "Apply Filter\ntune")
                depart_apply.depart_apply_filter.click()

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="Department Dashboard Apply Filter Button Assertion is Failed",
                          attachment_type=AttachmentType.PNG)
            print("Department Dashboard Apply Filter Button Assertion is Failed Due To : " + str(e))

        depart_view.filter.click()

        try:
            depart_value.depart_colm_values.click()

        except (StaleElementReferenceException) as e:
            self.filter_values = driver.find_element(By.XPATH, locator.filter_column)
            self.filter_values.click()

        try:
            depart_col.column_value.click()
        except (StaleElementReferenceException) as a:
            self.column_value = driver.find_element(By.XPATH, locator.filter_value)
            self.column_value.click()

        try:
            depart_oprt.depart_operator.click()
        except (StaleElementReferenceException) as b:
            self.operator = driver.find_element(By.XPATH, locator.filter_operator)
            self.operator.click()

        depart_oprt2 = depart_operator2_value2(driver)
        try:

            depart_oprt2.operator2.click()
        except (StaleElementReferenceException) as c:

            self.operator2 = driver.find_element(By.XPATH, locator.operator_value2)
            if (self.operator2.text == "Contains"):
                print("Department Dashboard Filter Operator Two Value Assertion is Passed")
                self.assertEqual(self.operator2.text, "Contains")
                self.operator2.click()

            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Department Dashboard Filter Operator Two Value Assertion is Failed",
                              attachment_type=AttachmentType.PNG)
                print("Department Dashboard Filter Operator Two Value Assertion is Failed Due To : " + str(c))
        try:
            depart_val.depart_value_field.send_keys("QA-Department")



        except Exception as e:
            self.depart_value = driver.find_element(By.XPATH, locator.value)
            if (self.depart_value.get_attribute("id") == "value"):
                print("Department Dashboard Filter Value Field Assertion is Passed")
                self.assertEqual(self.depart_value.get_attribute("id"), "value")
                self.depart_value.send_keys("QA-Department")
            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Department Dashboard Filter Value Field Assertion is Failed",
                              attachment_type=AttachmentType.PNG)
                print("Department Dashboard Filter Value Field Assertion is Failed Due To : " + str(e))

        try:

            depart_add_filter.add_filter.click()



        except (StaleElementReferenceException) as e:

            self.depart_add_filter = driver.find_element(By.XPATH, locator.filter_add)
            if (self.depart_add_filter.text == "Add\nadd"):

                print("Department Dashboard Add Filter Button Assertion is Passed")
                self.assertEqual(self.depart_add_filter.text, "Add\nadd")
                self.depart_add_filter.click()
            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Department Dashboard Add Filter Button Assertion is Failed",
                              attachment_type=AttachmentType.PNG)
                print("Department Dashboard Add Filter Button Assertion is Failed Due To : " + str(e))

        # try:
        #     if
        # print(depart_apply.depart_apply_filter.text)
        # print("Department Dashboard Apply Filter Button Assertion is Passed ")
        # self.assertEqual(depart_apply.depart_apply_filter.text, "Apply Filter\ntune")
        # depart_apply.depart_apply_filter.click()

        # except Exception as e:
        #         allure.attach(self.driver.get_screenshot_as_png(),
        #               name="Department Dashboard Apply Filter Button Assertion is Failed",
        #               attachment_type=AttachmentType.PNG)
        #     print("Department Dashboard Apply Filter Button Assertion is Failed Due To : " + str(e))


if __name__ == '__main__':
    unittest.main()
