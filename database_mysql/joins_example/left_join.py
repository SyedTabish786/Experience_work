
"""
Display customer Name and OrderId
"""


import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select c.customerName,o.orderNumber from orders o Left join customers c on c.customerName = "
            "c.customerName left join orders oc on o.orderNumber = oc.orderNumber ")

result = cur.fetchall()

for row in result:
    print(row)