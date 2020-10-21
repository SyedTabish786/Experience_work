"""
- Display the customerFirstName and customerLastName of customers whose state is equal to "CA"
"""
import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select contactFirstName,contactLastName,state from customers WHERE state = 'CA'")

result = cur.fetchall()

for row in result:
    print(row)
