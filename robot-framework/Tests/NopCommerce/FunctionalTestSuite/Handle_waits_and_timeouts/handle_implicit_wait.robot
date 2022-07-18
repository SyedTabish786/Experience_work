*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   http://demowebshop.tricentis.com/register
${homepagetitle}    Demo Web Shop. Register

*** Test Cases ***

Testing Implicit Wait
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST


    openBrw
    get_selenium_wait
    wait_4th_condition_implicit_wait
    get_selenium_wait


    Testing_implicit_wait_with_Assertions
    closeBrw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window
Testing_implicit_wait_with_Assertions
    title should be  ${homepagetitle}
#   Dropdown Boxes
    select radio button  Gender   M
    input text  name:FirstName  tabish
    input text  name:LastName   ishtiaq
    input text  id:Email    tabishishtiaq5@gmail.com
    input text  name:Passwordd   Zehra@786
    input text  name:ConfirmPassword    Zehra@786




closeBrw
   close browser

wait_4th_condition_implicit_wait
    set selenium implicit wait  10 seconds
get_selenium_wait
    ${implicittime}=    get selenium implicit wait
    log to console  ${implicittime}