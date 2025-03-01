#5-10-20 inserting record

import mysql.connector as conn

db=conn.connect(host='localhost',user='root',database='xii_cs')
myc=db.cursor()

a=1234
b='Deepak'
c='M'
d=12
e='D'

sql="insert into student values({},'{}','{}',{},'{}')".format(a,b,c,d,e)
print(sql)
myc.execute(sql)
db.commit()
print('Data saved')

myc.close()
db.close()

