
"""
How many employees are there in the company?
"""


import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select count(employeeNumber) from employees ")

result = cur.fetchall()

for row in result:
    print(row)