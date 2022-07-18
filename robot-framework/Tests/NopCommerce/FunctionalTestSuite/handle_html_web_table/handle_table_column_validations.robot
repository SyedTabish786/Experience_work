*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://testautomationpractice.blogspot.com/
${homepagetitle1}  Automation Testing Practice
${table}  xpath://table[@name='BookTable']
${row_data}    xpath://table[@name='BookTable']/tbody/tr[5]/td[1]
${column}   2
${column_data}   Author

*** Test Cases ***

Testing Validations of Columns In A Table
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Columns_validations_Of_Table
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_Columns_validations_Of_Table

    title should be  ${homepagetitle1}
    element should be visible   ${table}
    element should be enabled    ${table}
    ${data}=    table column should contain  ${table}   ${column}  ${column_data}
    log to console  ${data}




closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser























