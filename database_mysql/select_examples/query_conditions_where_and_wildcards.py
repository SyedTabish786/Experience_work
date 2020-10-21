import pymysql
from pprint import pprint

"""
        Which payments in any month and year are more than twice the average for that month and year (i.e. compare all  
	    payments in  Oct 2004 with the average payment for Oct 2004)? Order the results by the date of the payment. 
	    You will need to use the date functions.

"""

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from customers WHERE state = 'CA'")

result = cur.fetchall()

for row in result:
    print(row)
