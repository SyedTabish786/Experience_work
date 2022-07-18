*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://testautomationpractice.blogspot.com/
${homepagetitle1}  Automation Testing Practice
${table}  xpath://table[@name='BookTable']
${row_data}    xpath://table[@name='BookTable']/tbody/tr[5]/td[1]
${row}   4
${row_data_validation}   Learn JS

*** Test Cases ***

Testing Validations of Rows In A Table
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Rows_validations_Of_Table
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_Rows_validations_Of_Table

    title should be  ${homepagetitle1}
    element should be visible   ${table}
    element should be enabled    ${table}
    ${data}=    table row should contain  ${table}   ${row}   ${row_data_validation}
    log to console  ${data}




closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser























