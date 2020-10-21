
"""
List the products in each product line.

"""


import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select productLine, productName from products order by productLine")

result = cur.fetchall()

for row in result:
    print(row)




