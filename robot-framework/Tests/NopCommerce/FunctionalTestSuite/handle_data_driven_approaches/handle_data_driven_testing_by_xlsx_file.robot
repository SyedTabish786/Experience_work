*** Settings ***
Library     SeleniumLibrary
Resource    /Users/tabish/Documents/Projects/robot-framework/Resources/login_resources.robot

Library     DataDriver   /Users/tabish/Documents/Projects/robot-framework/TestData/login_credentials.xlsx   sheet_name=Sheet1
Suite Setup  openBrw1
Suite Teardown  closse_all_browser_windows
Test Template   Invalid_login

*** Test Cases ***

LoginTestwithExcel using ${username},${password}


*** Keywords ***

Invalid_login
    [Arguments]     ${username}     ${password}

     input_username  ${username}
     input_pass      ${password}
     click_login_btn
     error_message_on_invalid_credentials





























