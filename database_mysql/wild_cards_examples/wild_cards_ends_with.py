"""

- Display the customers whose customerFirstName ends with "ne"

"""

import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()



cur.execute("select * from customers  WHERE contactLastName like '%ne'")

result = cur.fetchall()

for row in result:
    print(row)