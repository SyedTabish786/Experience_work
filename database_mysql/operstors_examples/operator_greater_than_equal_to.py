

"""

Display the customers whose creditLimit is between 5000 and 10000
"""



import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur2 = mydb.cursor()

cur2.execute(" select * from customers WHERE creditLimit >= 5000 AND creditLimit <= 10000 ")

result = cur2.fetchall()

for row in result:
    print(row)
