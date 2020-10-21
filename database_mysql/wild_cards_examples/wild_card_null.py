"""

Display the customers whose addressLine2 is null
"""
import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()



cur.execute("select * from customers  WHERE addressLine2 IS null")

result = cur.fetchall()

for row in result:
    print(row)