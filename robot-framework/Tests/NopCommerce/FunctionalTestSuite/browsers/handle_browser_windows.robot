*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://www.google.com/
${url2}     https://www.bing.com/?toWww=1&redig=F1920657B4F3454A93D7F52A980B292F
${homepagetitle1}  Google
${homepagetitle2}   Bing

*** Test Cases ***

Testing Frames
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_browser_window1
    sleep   5
    openBrw12
    Testing_browser_window2

    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window
openBrw12
    open browser  ${url2}   ${browser}
    maximize browser window

Testing_browser_window1
    switch browser  1
    ${ti_tle1}=     get title
    log to console  ${ti_tle1}
    sleep   5
    title should be  ${homepagetitle1}
Testing_browser_window2
    switch browser  2
    ${ti_tle2}=     get title
    log to console  ${ti_tle2}
    sleep   5
    title should be  ${homepagetitle2}



closse_all_browser_windows
    close all browsers






close_current_Brw
# will only close only current browser window
   close browser

