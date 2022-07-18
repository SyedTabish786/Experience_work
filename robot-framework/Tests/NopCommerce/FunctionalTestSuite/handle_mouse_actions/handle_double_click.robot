*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://testautomationpractice.blogspot.com/
${homepagetitle1}  Automation Testing Practice
${btn}  xpath://button[contains(text(),'Copy Text')]

*** Test Cases ***

Testing Mouse Double Click Action
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Mouse_Action_Double_Click
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window

Testing_Mouse_Action_Double_Click

    title should be  ${homepagetitle1}
    element should be visible   ${btn}
    double click element   ${btn}






closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
