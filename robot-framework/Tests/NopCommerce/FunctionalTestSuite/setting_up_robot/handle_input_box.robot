*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/
${homepagetitle}  nopCommerce demo store
${loginbtn}  xpath: //a[contains(text(),'Log in')]
${loginpagetitle}  nopCommerce demo store. Login
${login_id}  tabishishtiaq5@gmail.com
${passwrd}  Zehra@786
${email_txt}  id:Email
${pass_txt}   id:Password
${login_btn}  xpath://button[contains(text(),'Log in')]


*** Test Cases ***

Testing Input Box
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST

    openBrw
    Login Test with Assertions
    closeBrw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window
Login Test with Assertions
    title should be  ${homepagetitle}
    click link    ${loginbtn}
    title should be  ${loginpagetitle}
#    ${"email_txt"}  set variable  id:Email
#    element should be visible  ${"email_txt"}
    element should be visible  ${email_txt}
    element should be enabled  ${email_txt}
    clear element text   ${email_txt}
    input text  ${email_txt}  ${login_id}
    element should be visible  ${pass_txt}
    element should be enabled  ${pass_txt}
    clear element text   ${pass_txt}

    input text  ${pass_txt}   ${passwrd}
    element should be visible  ${login_btn}
    click element  ${login_btn}

closeBrw
    close browser
