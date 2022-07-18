*** Settings ***
Library     SeleniumLibrary
Resource   /Users/tabish/Documents/Projects/robot-framework/Resources/login_resources.robot
Suite Setup  openBrw1
Suite Teardown  closse_all_browser_windows
Test Template   Invalid_login

*** Test Cases ***                username                password
Negative Testing
Valid_User_With_Empty_Password    admin@yourstore.com     ${EMPTY}
Valid_User_With_wrong_Password    admin@yourstore.com     xyz
Invalid_User_With_Valid_Password    admn@yourstore.com    admin
Invalid_User_With_Empty_Password    adm@yourstore.com     ${EMPTY}
Invalid_User_With_Invalid_Password    adm@yourstore.com     xyz



*** Keywords ***

Invalid_login
    [Arguments]     ${username}     ${password}

     input_username  ${username}
     input_pass      ${password}
     click_login_btn
     error_message_on_invalid_credentials





























