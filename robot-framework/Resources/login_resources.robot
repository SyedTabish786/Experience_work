*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}  chrome
${login_url}  https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
${homepagetitle}    Your store. Login
${email}    id:Email
${pass_wrd}  id:Password
${login_btn}   xpath://button[@type='submit']
${user_dashboard}   xpath://h1[contains(text(),'Dashboard')]
${dashboard}    Dashboard
${logout_btn}    xpath://a[contains(text(),'Logout')]
${logout_link}   Logout
${error_message}     Login was unsuccessful.
${logout}   xpath://strong[contains(text(),'Welcome, please sign in!')]
${logout_message}   Welcome, please sign in!


*** Keywords ***
openBrw1
    open browser  ${login_url}   ${browser}
    maximize browser window
    title should be  ${homepagetitle}

closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser

open_login_page
    go to    ${login_url}

input_username
    [Arguments]     ${username}
    input text  ${email}    ${username}

input_pass
    [Arguments]     ${password}
    input text   ${pass_wrd}    ${password}

click_login_btn
    click element   ${login_btn}
click_logout_btn
    click element    ${logout_btn}
error_message_on_invalid_credentials
    page should contain     ${error_message}

user_dashboard
    page should contain  ${dashboard}
    element should be visible    ${user_dashboard}


user_logout_message
    page should contain     ${logout_message}
    element should be visible   ${logout}
