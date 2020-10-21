
"""

Display the country name and count of customers for each country (This will display only 2 columns - country, count
	  of customers for that country)
"""



import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute(" SELECT country,COUNT(customerNumber) FROM customers WHERE country = 'USA';")

result = cur.fetchall()

for row in result:
    print(row)
