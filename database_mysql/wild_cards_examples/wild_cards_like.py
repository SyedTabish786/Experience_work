"""
- Display the customers whose phone starts with "03"
"""
import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()



cur.execute("select * from customers WHERE phone like '03%'")

result = cur.fetchall()

for row in result:
    print(row)
