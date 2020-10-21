import pymysql
from pprint import pprint



mydb = pymysql.Connect(host ="localhost" ,user = "root",password= "mysql1pwd",database="classicmodels")

host =mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from customers")
result = cur.fetchall()

for row in result:
    print(row)

cur.execute("select * from customers")
result2 = cur.fetchone()
for row in result2:
    print("This is fetch by using fetchone() function : " + str(row))