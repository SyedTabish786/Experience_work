*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   http://demowebshop.tricentis.com/register
${homepagetitle}    Demo Web Shop. Register

*** Test Cases ***

Testing Dropdown and List Boxes
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST
    2nd_condition_get_selenium_speed

    openBrw
    3rd_condition_selenium_timeout_time_set
    wait_3rd_condition_selenium_timeout

#    wait_1st_condition_sleep
#    wait_2nd_condition_selenium_speed
    Dropdown_and_List_Boxes_Test_with_Assertions
    2nd_condition_get_selenium_speed



    closeBrw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window
Dropdown_and_List_Boxes_Test_with_Assertions
    title should be  ${homepagetitle}
#   Dropdown Boxes
    select radio button  Gender   M
    input text  name:FirstName  tabish
    input text  name:LastName   ishtiaq
    input text  id:Email    tabishishtiaq5@gmail.com
    input text  name:Password   Zehra@786
    input text  name:ConfirmPassword    Zehra@786




closeBrw
   close browser
wait_1st_condition_sleep
    sleep   3
wait_2nd_condition_selenium_speed
#   applicable on each action of script execution on page element
    set selenium speed  15 seconds
2nd_condition_get_selenium_speed
    ${speed}=   get selenium speed
    log to console  ${speed}

wait_3rd_condition_selenium_timeout
    wait until page contains   Register
3rd_condition_selenium_timeout_time_set
    set selenium timeout  10 seconds


