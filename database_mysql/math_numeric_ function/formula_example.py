"""
List all payments greater than twice the average payment?
"""


import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from payments where amount > (select avg(amount) * 2 from payments)")

result = cur.fetchall()

for row in result:
    print(row)