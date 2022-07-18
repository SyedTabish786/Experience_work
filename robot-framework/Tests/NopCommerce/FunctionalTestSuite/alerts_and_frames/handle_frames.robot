*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/remote/codec/package-summary.html
${homepagetitle}   Overview

*** Test Cases ***

Testing Frames
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw
    Testing_frames

    close_current_Brw

*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window

Testing_frames
    title should be  ${homepagetitle}
    select frame    packageListFrame

    click link  org.openqa.selenium.cli
    unselect frame

    select frame    packageFrame
    click link  CliCommand.Executable
    unselect frame

    select frame    classFrame
    click link  Instance Methods



close_current_Brw
# will only close only current browser window
   close browser











