*** Settings ***
Library     SeleniumLibrary
Resource    /Users/tabish/Documents/Projects/robot-framework/Resources/resources.robot

*** Variables ***
${browser}   chrome
${url1}     https://demo.guru99.com/test/newtours/
${homepagetitle}  Welcome: Mercury Tours


*** Test Cases ***

Testing Keywords with Arguments and returnvalues
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    ${Pagetitle} =  launchBrowser   ${url1}  ${browser}
    log to console  ${Pagetitle}
    input text  name:userName  mercury
    input text  name:password   mercury
    sleep   5
    closse_all_browser_windows



