"""
What is the minimum payment received?
"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select  min(amount) as 'Minimum payment recieved' from payments")

result = cur.fetchall()

for row in result:
    print(row)
