*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}   http://demowebshop.tricentis.com/register
${url2}   http://automationpractice.com/index.php
${homepagetitle}    Demo Web Shop. Register

*** Test Cases ***

Testing Implicit Wait
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_implicit_wait_with_Assertions
    openBrw2
    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window
openBrw2
    open browser  ${url2}   ${browser}
    maximize browser window
Testing_implicit_wait_with_Assertions
    title should be  ${homepagetitle}
#   Dropdown Boxes
    select radio button  Gender   M
    input text  name:FirstName  tabish
    input text  name:LastName   ishtiaq
    input text  id:Email    tabishishtiaq5@gmail.com
    input text  name:Password   Zehra@786
    input text  name:ConfirmPassword    Zehra@786




close_current_Brw
# will only close only current browser window
   close browser
closse_all_browser_windows
    close all browsers

