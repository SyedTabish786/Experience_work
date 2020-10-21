"""
List the product lines that contain 'Cars'

"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select productLine from productlines where productLine like '%Cars%'")

result = cur.fetchall()

for row in result:
    print(row)

