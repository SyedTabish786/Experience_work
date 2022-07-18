*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://testautomationpractice.blogspot.com/
${homepagetitle1}  Automation Testing Practice
${table}  xpath://table[@name='BookTable']
${row_data}    xpath://table[@name='BookTable']/tbody/tr[5]/td[1]

*** Test Cases ***

Testing Number of Columns In A Table
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Count_Number_Columns_Of_Table
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_Count_Number_Columns_Of_Table

    title should be  ${homepagetitle1}
    element should be visible   ${table}
    element should be enabled    ${table}
    element should be visible   ${row_data}
    ${data_row5}=     get text   ${row_data}
    log to console  ${data_row5}







closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser























