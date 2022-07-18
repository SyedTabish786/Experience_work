*** Settings ***
Library  DatabaseLibrary    #https://franz-see.github.io/Robotframework-Database-Library/api/0.5/DatabaseLibrary.html
Library  OperatingSystem

Suite Setup  Connect To Database    pymysql  ${DBname}  ${DBUser}   ${DBPass}   ${DBHost}   ${DBPort}
Suite Teardown  Disconnect From Database

*** variables ***
${DBname}   sakila
${DBUser}   root
${DBPass}   mysql1pwd
${DBHost}   localhost
${DBPort}   3306

${table_name}   person
${table_name2}   pers_ons
${first_name}    select id from sakila.person where first_name="chris"
${first_name2}    select id from sakila.person where first_name="mogambo"
${row_count}     select * from sakila.person where first_name="xyz";
${row_count2}     select * from sakila.person where first_name="george";
${x_value2}  1
${row_count3}     select * from sakila.person where first_name="marry";
${x_value3}  0
${row_count4}     select * from sakila.person where first_name="jhon";
${x_value4}  5



*** Test Cases ***
Verification Of Table Presents In Database
    table must exist    ${table_name}
Verification Of Table Not Presents In Database
    table must exist    ${table_name2}

Verification Of Specific Record Presents In Person Table
    check if exists in database  ${first_name}


Verification Of Specific Record Not Presents In Person Table
    check if not exists in database  ${first_name2}

Verification Of Row Count is Zero
    row count is 0  ${row_count}

Verification Of Row Count Is Equal To Some Value
    row count is equal to x  ${row_count2}      ${x_value2}

Verification Of Row Count Is Greater Than Some Value
    row count is greater than x  ${row_count3}      ${x_value3}

Verification Of Row Count Is Less Than Some Value
    row count is less than x  ${row_count4}      ${x_value4}

Update a record in person table
     ${out_put}=     Execute SQL String  update person set first_name="jio" where id=107;
     log to console  ${out_put}
     should be equal as strings  ${out_put}  None

Retrieve a record from person table
     @{queryResults}=       query   select * from person;
     log to console    many @{queryResults}



