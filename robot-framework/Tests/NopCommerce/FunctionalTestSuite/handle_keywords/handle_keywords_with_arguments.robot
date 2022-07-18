*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://demo.guru99.com/test/newtours/
${homepagetitle1}  Welcome: Mercury Tours


*** Test Cases ***

Testing Keywords with Arguments
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    launchBrowser   ${url1}  ${browser}
    title should be  ${homepagetitle1}
    input text  name:userName  mercury
    input text  name:password   mercury

    sleep   5


    closse_all_browser_windows

*** Keywords ***
launchBrowser
    [Arguments]  ${appurl1}  ${appbrowser}
    open browser  ${appurl1}   ${appbrowser}
    maximize browser window


closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
