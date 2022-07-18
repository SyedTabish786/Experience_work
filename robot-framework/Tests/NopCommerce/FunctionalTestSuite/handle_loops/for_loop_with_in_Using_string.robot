*** Test Cases ***

ForLoop_with_IN_with_string_using_single_spacing1
    FOR   ${i}   IN  tabish zaigham kanwal sumbul
            log to console  ${i}
    END
ForLoop_with_IN_with_string_using_double_spacing2
    FOR   ${i}   IN  tabish  zaigham  kanwal  sumbul
            log to console  ${i}
    END
ForLoop_with_IN_with_stringlist_using_single_spacing3
    @{nameslist1}    create list  tabish zaigham kanwal sumbul
    FOR   ${i}   IN  @{nameslist1}
            log to console  ${i}
    END
ForLoop_with_IN_with_stringlist_using_double_spacing4
    @{nameslist1}    create list  tabish  zaigham  kanwal  sumbul
    FOR   ${i}   IN  @{nameslist1}
            log to console  ${i}
    END



ForLoop_with_IN_with_string_using_single_spacing5
    FOR   ${i}   IN  table chair computer radio tv
            log to console  ${i}
    END
ForLoop_with_IN_with_string_using_double_spacing6
    FOR   ${i}   IN  table  chair  computer  radio  tv
            log to console  ${i}
    END
ForLoop_with_IN_with_stringlist_using_single_spacing7
    @{nameslist2}    create list  table chair computer radio tv
    FOR   ${i}   IN  @{nameslist2}
            log to console  ${i}
    END
ForLoop_with_IN_with_stringlist_using_double_spacing8
    @{nameslist2}    create list  table  chair  computer  radio  tv
    FOR   ${i}   IN  @{nameslist2}
            log to console  ${i}
    END