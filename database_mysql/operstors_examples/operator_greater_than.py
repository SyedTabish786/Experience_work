
"""
- Display the customers whose creditLimit is greater than 10000

"""


import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from customers  WHERE creditLimit > '10000'")

result = cur.fetchall()

for row in result:
    print(row)
