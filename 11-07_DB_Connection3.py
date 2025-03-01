#11-07
#Demo to fetch data from MySQL using Python

import mysql.connector as con
kvc=int(input('Enter kvcode to find the details :'))

mydb=con.connect(host='localhost', user='root', password='pankaj', database='xibtp')
c=mydb.cursor()
sql='select * from kv where kvcode='+str(kvc)
c.execute(sql)
myresult=c.fetchall()

#print('No of records found ',c.rowcount)
for rec in myresult:
    print('KV Code is ',rec[1])
    print('Name is ',rec[2])
    print('Zone code is ',rec[3])
    print('Region code is ',rec[4])
    print('Station code is ',rec[5])
