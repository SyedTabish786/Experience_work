*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm
${homepagetitle}  Selenium - Automation Practice Form
${male}   xpath://input[1][@name='sex']
${female}  xpath://input[2][@name='sex']
${experience}   xpath://tbody/tr[4]/td[2]/span[3]/input[1]

*** Test Cases ***

Testing Radio Buttons and Check Boxes
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST

    openBrw
    Radio Buttons and Check Boxes Test with Assertions
    closeBrw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window
Radio Buttons and Check Boxes Test with Assertions
    title should be  ${homepagetitle}
    element should be visible   ${male}
    element should be enabled   ${male}
    click element   ${male}
    element should be visible   ${experience}
    element should be enabled   ${experience}
    click element   ${experience}
    select checkbox   Manual Tester
    select checkbox   Automation Tester
    unselect checkbox   Manual Tester
#     select radio button    RESULT_CheckBox-8_1  1
closeBrw
    close browser

