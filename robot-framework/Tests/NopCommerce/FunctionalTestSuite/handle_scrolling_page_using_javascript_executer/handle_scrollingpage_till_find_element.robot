*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://www.countries-ofthe-world.com/flags-of-the-world.html
${homepagetitle1}  Country flags of the world with images and names
${flag}  xpath://tbody/tr[112]/td[2]

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
    scroll element into view    ${flag}







closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
