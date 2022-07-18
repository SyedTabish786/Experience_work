*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
${homepagetitle1}  Demo 2: Drag and drop
${src_btn}  id:box6
${trgt_box}     id:box106

*** Test Cases ***

Testing Mouse Double Click Action
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Mouse_Drag_Drop_Action
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window

Testing_Mouse_Drag_Drop_Action

    title should be  ${homepagetitle1}
    element should be visible   ${src_btn}
    drag and drop   ${src_btn}  ${trgt_box}






closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
