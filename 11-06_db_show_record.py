#10-06_db_connectivity
#Mysql - Python connectivity

import mysql.connector as con

mydb=con.connect(host='localhost', user='root', passwd='pankaj', database='xibtp')
mycursor=mydb.cursor()
ad=int(input('Enter admission number to search :'))
sql='select admno, name, sex, class, sec  from student where admno='+str(ad)
mycursor.execute(sql)                   #executing SQL
myresult = mycursor.fetchall()          #fetching data from db
if mycursor.rowcount==0:
    print('Sorry!!! This admission number does not exist in the database')
else:
    for data in myresult:
        print('Admission nmumber is ',data[0])
        print('Name is ',data[1])
        if data[2].upper()=='M':
            s='Male'
        elif data[2].upper()=='F':
            s='Female'
        else:
            s='Other'
        print('Gender is ',s)
        print('Class and Section is ',data[3],'-',data[4])

mydb.close()                                                    