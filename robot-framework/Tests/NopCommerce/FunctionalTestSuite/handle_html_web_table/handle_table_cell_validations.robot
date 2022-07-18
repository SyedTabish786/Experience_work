*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://testautomationpractice.blogspot.com/
${homepagetitle1}  Automation Testing Practice
${table}  xpath://table[@name='BookTable']
${column}       4
${row}      2
${cell_data}    Animesh

*** Test Cases ***

Testing Validations of Cells In A Table
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Cells_validations_Of_Table
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_Cells_validations_Of_Table

    title should be  ${homepagetitle1}
    element should be visible   ${table}
    element should be enabled    ${table}

    table cell should contain  ${table}   ${column}  ${row}   Animesh






closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser























