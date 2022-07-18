*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   http://demo.automationtesting.in/Windows.html
${homepagetitle}  Frames & windows
${clickbtn}     xpath://body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/button[1]
${select_opt}   //span[contains(text(),'Support')]

*** Test Cases ***

Testing Frames
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw
    Testing_frames
    sleep   5
    close_current_Brw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window

Testing_frames
    title should be  ${homepagetitle}
    click element   ${clickbtn}
    switch window   title=Selenium
    click element   ${select_opt}







close_current_Brw
# will only close only current browser window
   close browser
