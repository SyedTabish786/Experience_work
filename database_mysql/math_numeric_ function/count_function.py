
"""

Display the COUNT of customers whose country is USA
"""





import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute(" SELECT COUNT(customerNumber) FROM customers WHERE country = 'USA';")

result = cur.fetchall()

for row in result:
    print(row)
