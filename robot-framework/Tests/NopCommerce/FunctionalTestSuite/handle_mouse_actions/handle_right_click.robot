*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://swisnl.github.io/jQuery-contextMenu/demo.html
${homepagetitle1}  jQuery contextMenu (2.x)
${btn}  xpath://span[contains(text(),'right click me')]

*** Test Cases ***

Testing Mouse Righ Click Action
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Mouse_Action_Right_Click
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window

Testing_Mouse_Action_Right_Click

    title should be  ${homepagetitle1}
    element should be visible   ${btn}
    open context menu   ${btn}






closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
