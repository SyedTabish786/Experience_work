*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm
${homepagetitle}  Selenium - Automation Practice Form
*** Test Cases ***

Testing Dropdown and List Boxes
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST

    openBrw
    Dropdown_and_List_Boxes_Test_with_Assertions
    closeBrw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window
Dropdown_and_List_Boxes_Test_with_Assertions
    title should be  ${homepagetitle}
#   Dropdown Boxes
    select from list by label  continents  Africa
    sleep   3
    select from list by index    continents  1
    sleep   3
#    select from list by value    continents  Radio-2
#    sleep   3


#    Listboxes
    select from list by label   selenium_commands  Switch Commands
    sleep   3
    select from list by index   selenium_commands  4
    sleep   3
    unselect from list by index     selenium_commands  4
    sleep   3
#    select from list by value    name or id  value

closeBrw
   close browser

