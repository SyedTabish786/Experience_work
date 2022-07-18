*** Settings ***

Library     SeleniumLibrary

Suite Setup  openBrw1
Suite Teardown  closse_all_browser_windows
Test Template
*** Variables ***
${browser}  chrome
${login_url}  https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
${homepagetitle}    Your store. Login

*** Test Cases ***
Testing Log To Console
    Log To Console  [Here Test Case Script] Will Successfully Execute



*** Keywords ***
openBrw1
    open browser  ${login_url}   ${browser}
    maximize browser window
    title should be  ${homepagetitle}
    log to console  [Suit Setup] Successfully Run Once At The Beginning Of Script

closse_all_browser_windows
    close all browsers
    log to console  [Teardown] Successfully Run Once At The End Of Script

close_current_Brw
# will only close only current browser window
   close browser








Invalid_login
    [Arguments]     ${username}     ${password}

     input_username  ${username}
     input_pass      ${password}
     click_login_btn
     error_message_on_invalid_credentials
