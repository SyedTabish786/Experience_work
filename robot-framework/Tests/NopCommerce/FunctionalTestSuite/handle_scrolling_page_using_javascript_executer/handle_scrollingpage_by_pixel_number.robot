*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://www.countries-ofthe-world.com/flags-of-the-world.html
${homepagetitle1}  Country flags of the world with images and names
#${btn}  xpath://span[contains(text(),'right click me')]

*** Test Cases ***

Testing Scrollingpage by pixel number
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Scrollingpage_by_pixel_number
    sleep   5


    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window


Testing_Scrollingpage_by_pixel_number

    title should be  ${homepagetitle1}
    execute javascript  window.scrollTo(0,2500)







closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
