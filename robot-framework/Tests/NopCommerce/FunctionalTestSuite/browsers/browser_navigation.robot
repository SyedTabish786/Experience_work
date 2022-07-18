*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://www.google.com/
${url2}     https://www.bing.com/?toWww=1&redig=F1920657B4F3454A93D7F52A980B292F
${homepagetitle1}  Google
${homepagetitle2}   Bing

*** Test Cases ***

Testing Browser Navigation
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_browser_navigation
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window

Testing_browser_navigation
    ${loc} =    get location
    log to console      ${loc}
    title should be  ${homepagetitle1}
    go to   https://www.bing.com/?toWww=1&redig=F1920657B4F3454A93D7F52A980B292F
    ${loc} =    get location
    log to console      ${loc}
    go back
    ${loc} =    get location
    log to console      ${loc}




closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser

