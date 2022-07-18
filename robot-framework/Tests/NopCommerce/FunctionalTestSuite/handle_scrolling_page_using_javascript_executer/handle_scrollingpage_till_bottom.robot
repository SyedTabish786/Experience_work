*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}   chrome
${url1}     https://www.countries-ofthe-world.com/flags-of-the-world.html
${homepagetitle1}  Country flags of the world with images and names


*** Test Cases ***

Testing_Scroll_Page_To_Bottom
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw1
    Testing_Scroll_Page_To_Bottom
    Testing_page






    closse_all_browser_windows

*** Keywords ***
openBrw1
    open browser    ${url1}   ${browser}
    maximize browser window
    sleep   2



Testing_Scroll_Page_To_Bottom

     title should be  ${homepagetitle1}
     execute javascript  window.scrollTo(0,document.body.scrollHeight)   # Move to end of page
     sleep   2


Testing_page
     execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #Move to starting of page
     sleep   2










closse_all_browser_windows
    close all browsers

close_current_Brw
# will only close only current browser window
   close browser
