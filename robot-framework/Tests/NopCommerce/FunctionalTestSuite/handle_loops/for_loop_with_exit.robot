*** Test Cases ***


ForLoop_with_exit_singlespace
    @{nameslist1}    create list  1 2 3 4 5 6
    FOR   ${i}   IN  @{nameslist1}
            log to console  ${i}
            exit for loop if  ${i}==2
    END


ForLoop_with_exit_doublespace
    @{nameslist1}    create list  1   2   3   4   5   6
    FOR   ${i}   IN  @{nameslist1}
            log to console  ${i}
            exit for loop if  ${i}==2
    END