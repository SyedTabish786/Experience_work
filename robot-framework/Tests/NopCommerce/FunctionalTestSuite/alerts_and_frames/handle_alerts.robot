*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${browser}   chrome
${url}   https://testautomationpractice.blogspot.com/
${homepagetitle}    Automation Testing Practice
${alrt_btn}     xpath:  //button[contains(text(),'Click Me')]


*** Test Cases ***

Testing alerts acceptance
    [Documentation]  This Test Will Passes
    [Tags]  REGRESSION TEST


    openBrw
    Testing_alert_and_frames
    sleep   3
    handle_alert_acceptance
    sleep   3
    close_current_Brw




Testing alerts dismisal
    [Documentation]  This Test will passes
    openBrw
    Testing_alert_and_frames
    sleep   3
    handle_alert_dismisal
    sleep   3
    close_current_Brw

Testing alerts asit is
    [Documentation]  This Test will passes
    openBrw
    Testing_alert_and_frames
    sleep   3
    handle_alert_as_it_is
    sleep   3
    close_current_Brw

Testing alert message presence
    [Documentation]  This Test will passes
    openBrw
    Testing_alert_and_frames
    sleep   3
    alert_box_message_presence
    close_current_Brw

Testing alert message presence
    [Documentation]  This Test will fails
    openBrw
    Testing_alert_and_frames
    sleep   3
    alert_box_message_not_present
    close_current_Brw









*** Keywords ***
openBrw
    open browser  ${url}   ${browser}
    maximize browser window

Testing_alert_and_frames
    title should be  ${homepagetitle}
    click element   ${alrt_btn}

close_current_Brw
# will only close only current browser window
   close browser
handle_alert_acceptance
     handle alert    accept
handle_alert_dismisal
    handle alert    dismiss
handle_alert_as_it_is
    handle alert    leave
alert_box_message_presence
    alert should be present     Press a button!
alert_box_message_not_present
    alert should not be present     Press a button!

