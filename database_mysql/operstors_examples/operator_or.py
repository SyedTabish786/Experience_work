
"""
Display the customers whose customerFirstName is equal to "Julie" OR whose customerLastName is equal to "Murphy"
"""



import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from customers WHERE contactFirstName = 'Julie' OR contactLastName = 'Murphy'")

result = cur.fetchall()

for row in result:
    print(row)
