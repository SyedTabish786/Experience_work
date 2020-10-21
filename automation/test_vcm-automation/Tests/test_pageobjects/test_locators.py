class locator(object):
#login page locators

    logo = "//img[1]"
    login_drop = '//*[@id="logbt"]'
    user_name = "//input[@id = 'username']"
    password= "//input[@id = 'password']"

    login_button = "//button/span[text()=' Login ']"




#Home page locators
    home_icon = "//i[text() = 'home']"



#User Management homepage locators
    #user_management_icon = "//i[contains(text(),'supervisor_account')]"
    user_management_icon = "//div[@class='flex xs6 sm3 md2 lg2'][2]//i[contains(text(),'supervisor_account')]"
    application_role = "//div[contains(text(),'Application Role')]"
#Add application roles locators
    add= "//span[contains(text(),'Add New')]"
    add_field = "//input[@id='moduleIds']"
    add_dropdown_value1 = "//div[contains(text(),'Vendor Compliance')]"
    add_dropdown_value2 = "//div[contains(text(),'Meeting Management')]"
    add_dropdown_value3 = "//div[contains(text(),'Change Management')]"
    add_dropdown_closure = "//div[contains(@class,'flex sm12')]//div[3]"
    add_name = "//input[@id='name']"
    add_description = "//textarea[@id='description']"
    add_continue = "//span[contains(text(),'Continue')]"
    add_keyword_search = "//input[@id='search']"
    clear_search = "//div[contains(@class,'pt-2')]//div//div[@class='v-input__icon v-input__icon--clear']"
    permission_option1 = "//div[contains(@class,'v-treeview-node__content')]//span[contains(text(),'Vendor Compliance')]"
    permission_option2 = "//div[contains(@class,'v-treeview-node__content')]//span[contains(text(),'Meeting Management')]"
    permission_option3 = "//body/div[@id='app']/div[@id='app']/div[@class='v-application--wrap']/div[@class='layout wrap']/main[@class='v-content contentbg main-body-container usermanagement']/div[@class='v-content__wrap']/div[@class='container container--fluid']/div[@class='flex xs12 flex xs12']/div[@class='v-card v-sheet theme--light elevation-1']/div[@class='v-card__text']/form[@id='Form']/fieldset[@class='base-fieldset']/div[@class='layout wrap']/div[@class='main']/div[@class='v-stepper my-stepper v-stepper--is-booted v-stepper--alt-labels theme--light']/div/div[@class='v-stepper__items']/div[@class='v-stepper__content']/div[@class='v-stepper__wrapper']/div/div[@class='subheading mt-3 mb-3']/div[@class='pt-2']/div[@class='v-treeview v-treeview--dense theme--light']/div[3]/div[1]/i[1]"
    permission_option1_selection = "//div[contains(@class,'pt-2')]//div[1]//div[1]//i[2]"
    permission_option2_selection = "//*[@id='Form']/fieldset/div[1]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/i[2]"
    #permission_option3_selection = "//div[contains(@class,'pt-2')]//div[3]/div/i[2]"
    permission_option3_selection = '//*[@id="Form"]/fieldset/div[1]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[3]/div/i[2]'
    add_finalize = "//span[@class='v-btn__content'][contains(text(),'Add')]"
    check_add_role = "//td[contains(text(),'Automation User')]"
# DashBoard Locators

    dashboard_search = "//label[@class='v-label theme--light']/following::input[1]"
    dashboard_export =  "//span[contains(text(),'Export')]"
    export_pdf = "//div[contains(text(),'PDF')]"
    export_excel = "//div[contains(text(),'Excel')]"


    dashboard_filter = "//span[contains(text(),'Filter')]"

    filter_column = "//input[@id='selectedColumn']"

    filter_value = "//div[contains(text(),'Name')]"
    filter_operator = "//input[@id='selectedOperator']"
    operator_value1 = "//div[contains(text(),'Equals')]"
    operator_value2 = "//div[contains(text(),'Contains')]"
    page_selection = "//div[@class='v-input select-pages-per-row v-input--is-label-active v-input--is-dirty theme--light v-text-field v-text-field--is-booted v-select']//i[@class='v-icon notranslate mdi mdi-menu-down theme--light']"
    page_selection_value1 ="//div[@class='v-menu__content theme--light menuable__content__active']//div[3]"
    page_selection_value2 = "//div[@class='v-list-item primary--text v-list-item--active v-list-item--link theme--light']/span"
    value = "//input[@id='value']"
    filter_add = "//button[@class='mt-2 ml-2 alpha_background_color_theme_medium text-white v-btn v-btn--depressed v-btn--rounded theme--light v-size--default']"
    apply_filter = "//button[@class='link_color_blue_background text-white header-apply-filter-btn v-btn v-btn--depressed v-btn--rounded theme--light v-size--small']"
    clear_filter = "//span[contains(text(),'Clear All Filter')]"
    page_count = "//span[@class='page-header-filter-pager-text']"
    next_page = "//i[contains(text(),'arrow_right')]"
    previous_page = "//i[contains(text(),'arrow_left')]"
    name_sort = "//i[contains(text(),'sort')]"
    description_sort = "//th[3]//span[2]//span[1]//i[1]"
    column_select_deselect = "//i[@class='v-icon notranslate v-icon--right material-icons theme--light grey--text text--darken-2']"
    name_column = "//label[contains(text(),'Name')]"
    description_column = "//label[contains(text(),'Description')]"
    edit_profile = "//td[contains(text(),'Automation User')]//..//span[1]/i"
    edit_profile_continue = "//span[contains(text(),'Continue')]"
    edit_profile_save_button = "//span[contains(text(),'Save')]"
    profile_view = "//td[contains(text(),'Automation User')]//..//span[2]/i"
    previous_button = "//span[contains(text(),'Previous')]"
    back_button = "//span[contains(text(),'Back')]"
    more_option = "//td[contains(text(),'Automation User')]//..//div/following-sibling::i"
    deactivate_profile = "//td[contains(text(),'Automation User')]/ancestor::div//div[contains(text(),'Deactivate')]"
    #deactivate_notification = "//span[contains(text(),'Deactivate')]"
    deactivate_notification = "//button[@class='swal2-confirm swal2-styled']"
    restore_profile = "//div[contains(text(),'Restore')]"

    delete_profile = "//div[@class='v-menu__content theme--light menuable__content__active menu-drop-shadow table-actions-menu']//div[contains(text(),'Delete')]"
    footer_page2 = "//button[@class='v-pagination__item']"
    footer_page1 = "//button[@class='v-pagination__item v-pagination__item--active primary']"
    footer_next_page = "//i[@class='v-icon notranslate mdi mdi-chevron-right theme--light']"
    footer_previous_page = "//i[@class='v-icon notranslate mdi mdi-chevron-left theme--light']"

    department = "//div[text()='Department']"
    add_depart = "//span[contains(text(),'Add New')]"
    add_depart_name = "//input[@id='name']"
    depart_head = "//input[@id='applicationUserId']"
    head_drop_down = "//span[contains(text(),'Admin Super')]"
    add_depart_finalize = "//span[@class='v-btn__content'][contains(text(),'Add')]"
    depart_dashboard_search = "//label[@class='v-label theme--light']/following::input[1]"









    application_user = "//div[text()='Application User']"
    user_group = "//div[text()='User Group']"
    settings = "//div[text()='Settings']"
    scorecard_parameters = "//div[text()=' Scorecard Parameter ']"
    scorecard            = "//div[text()=' Scorecard ']"





    vendor_compliance_icon = "//i[text()='loyalty']"
    item_management_icon = "//i[text()='widgets']"
    setup_icon ="//i[text()='settings_input_component']"
    e_e_f_icon = "//i[text()='brightness_high']"
    o_m_icon = "//i[text()='gps_fixed']"
    m_m_icon = "//i[text()='person_pin']"
    epmo_icon= "//i[text()='business_center']"
    cm_icon = "//i[text()='loop']"
    ps_icon = "//i[text()='settings']"
    tm_icon = "//i[text()='playlist_add_check']"
    pd_icon = "//div[text()='Product Development']"
    logistic_icon = "//i[text()='directions_boat']"
    lm_icom = "//i[text()='label']"


#Vendor Compliance homepage locators
    suppliers = "//div[text()='Supplier']"
    factory =  "//div[text()='Factory']"
    evaluation = "//div[text()='Evaluation']"
    audit      = "//div[text()=' Audit ']"
    audit_configuration = "//div[text()='Audit Configuration ']"
    severity_level = "//div[text()=' Severity Level ']"
    rating_system = "//div[text()=' Rating System ']"
    audit_tempelate = "//div[text()=' Audit Template ']"
    setting_s = "//div[text()='Settings']"
    agency = "//div[text()=' Agency ']"
    certification = "//div[text()=' Certification ']"
    document_sec = "//div[text()=' Document Section ']"
    document = "//div[text()=' Document ']"
    entity = "//div[text()=' Entity Type ']"
    attribute_type = "//div[contains(text(),' Green Attribute Type ')]"
    att_type = '//*[@id="app"]/div[3]/div/nav/div[1]/div/div[2]/div[2]/div/a[6]/div[2]'
    green_attribute = "//div[text()=' Green Attribute ']"
    material_type = "//div[text()=' Material Type ']"

    policies = "//div[text()=' Documents / Policies ']"
    s_f_attributes = "//div[text()=' Supplier / Factory Attributes ']"


#Item management homepage locators
    item_group = "//a[@href='/itemmanagement/3/itemgroup']"
    attribute_groups = "//a[@href='/itemmanagement/3/attributeGroups']"





