*** Settings ***
Library     SeleniumLibrary


*** Keywords ***
launchBrowser
    [Arguments]  ${appurl1}  ${appbrowser}
    open browser  ${appurl1}   ${appbrowser}
    maximize browser window
    ${homepagetitle} =  get title
    [return]    ${homepagetitle}

closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser

