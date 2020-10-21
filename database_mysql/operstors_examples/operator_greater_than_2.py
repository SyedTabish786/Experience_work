"""
Report those payments greater than $100,000.
"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from payments where amount > 100000")

result = cur.fetchall()

for row in result:
    print(row)
