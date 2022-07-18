*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://testautomationpractice.blogspot.com/
${homepagetitle1}  Automation Testing Practice
${table}  xpath://table[@name='BookTable']
${table_row}    xpath://table[@name='BookTable']/tbody/tr

*** Test Cases ***

Testing Number of Rows In A Table
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Count_Number_Rows_Of_Table
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_Count_Number_Rows_Of_Table

    title should be  ${homepagetitle1}
    element should be visible   ${table}
    element should be enabled    ${table}
    ${row_count}=     get element count   ${table_row}
    log to console  ${row_count}







closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser























