"""
Report total payments for October 28, 2004.
"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from payments where paymentDate = '2004-10-28'")

result = cur.fetchall()

for row in result:
    print(row)
