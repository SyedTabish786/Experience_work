*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://demo.guru99.com/test/newtours/
${homepagetitle1}  Welcome: Mercury Tours
${links}  xpath://a

*** Test Cases ***

Testing Link Extraction From Page
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_link_Extraction_from_page
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_link_Extraction_from_page

    title should be  ${homepagetitle1}
    ${allinkscount}=    get element count   ${links}
    log to console  ${allinkscount}
    @{linklistitems}    create list
    ${strip}    @{linklistitems}.strip(" ",1)

    FOR  ${i}    IN RANGE  1   ${allinkscount}+1
       ${linkstext}=   get text    xpath:(//a)[${i}]

        log to console  ${linkstext}
    END





closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
