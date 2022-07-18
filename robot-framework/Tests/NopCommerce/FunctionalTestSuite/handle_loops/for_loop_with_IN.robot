*** Test Cases ***

ForLoop_with_IN_using_single_spacing
    FOR   ${i}   IN  1 2 3 4 5 6 7 8
            log to console  ${i}
    END

ForLoop_with_IN_using_double_spacing
    FOR   ${i}   IN   1  2  3  4  5  6  7  8
            log to console  ${i}
    END