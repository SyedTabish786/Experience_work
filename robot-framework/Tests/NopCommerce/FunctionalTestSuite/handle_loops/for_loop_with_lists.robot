*** Test Cases ***

ForLoop_with_list_in_singlespacing
    @{items}    create list  1 2 3 4 5 6 7 8
    FOR   ${i}   IN  @{items}
            log to console  ${i}
    END

ForLoop_with_list_in_doublespacing
    @{items}    create list  1  2  3  4  5  6  7  8
    FOR   ${i}   IN  @{items}
            log to console  ${i}
    END