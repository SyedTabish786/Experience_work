*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://demo.guru99.com/test/newtours/
${homepagetitle1}  Welcome: Mercury Tours
${links}  xpath://a

*** Test Cases ***

Testing Link Count On Page
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_link_count_on_page
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_link_count_on_page

    title should be  ${homepagetitle1}
    ${allinkscount}=    get element count   ${links}
    log to console  ${allinkscount}






closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
