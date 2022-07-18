*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/
*** Test Cases ***
LoginTest
    [Documentation]  NOPCOMMERCE TEST
    [Tags]  REGRESSION TEST


    Open Browser   ${url}  ${browser}
    click link    xpath: //a[contains(text(),'Log in')]
    input text    id:Email  tabishishtiaq5@gmail.com
    input text    id:Password  Zehra@786
    click element  xpath://button[contains(text(),'Log in')]
    close Browser


*** Keywords ***
