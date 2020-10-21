"""

- Display the customers whose customerName starts with "LA"

"""
import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()



cur.execute("select * from customers WHERE customerName like 'LA%'")

result = cur.fetchall()

for row in result:
    print(row)