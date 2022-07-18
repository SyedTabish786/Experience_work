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




*** Test Cases ***

Delete a record from person table
     ${out_put}=     Execute SQL String  delete from person;
     log to console  ${out_put}
     should be equal as strings  ${out_put}  None

