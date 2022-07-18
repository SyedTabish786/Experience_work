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
Inserting Multiple Data In Person Table
    ${out_put}=     Execute SQL Script  /Users/tabish/Documents/Projects/robot-framework/TestData/db_data.sql
    log to console  ${out_put}
    should be equal as strings  ${out_put}  None


