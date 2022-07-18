*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://opensource-demo.orangehrmlive.com/
${homepagetitle1}  OrangeHRM
${page}     xpath://div[@id='divLogo']/img
${username_input}     id:txtUsername
${username_input_data}    Admin
${password_input}   id:txtPassword
${password_input_data}    admin123
${login_btn}    id:btnLogin
${screen_shot_path}     screen_shoot/page.png

*** Test Cases ***

Testing Browser Navigation
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_browser_navigation
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser  ${url1}   ${browser}
    maximize browser window

Testing_browser_navigation

    title should be  ${homepagetitle1}
    element should be visible   ${page}
    input text  ${username_input}   ${username_input_data}
    input text  ${password_input}   ${password_input_data}
    capture page screenshot     ${screen_shot_path}




closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
