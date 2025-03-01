#5-10-20 connectivity

import mysql.connector as conn

db=conn.connect(host='localhost',user='root')
myc=db.cursor()
sql='show databases'
myc.execute(sql)
myresult=myc.fetchall()
print(myresult)

myc.close()
db.close()
