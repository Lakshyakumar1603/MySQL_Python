#5-10-20 inserting record

import mysql.connector as conn

db=conn.connect(host='localhost',user='root',database='xii_cs')
myc=db.cursor()

a=int(input('Enter your admission number :'))
b=input('Enter your name :')
c=input('Enter your gender (M/F) :')
d=int(input('Enter your class :'))
e=input('Enter your section (A/B/C/D) :')

sql=f"insert into student values({a},'{b.upper()}','{c.upper()}',{d},'{e.upper()}')" 
print(sql)
myc.execute(sql)
db.commit()
print('Data saved')

myc.close()
db.close()

