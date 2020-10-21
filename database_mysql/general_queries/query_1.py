
"""

Prepare a list of offices sorted by country, state, city.
"""




import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select * from offices order by state,country and city ")

result = cur.fetchall()

for row in result:
    print(row)