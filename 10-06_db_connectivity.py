#10-06_db_connectivity
#Mysql - Python connectivity

import mysql.connector as con

mydb=con.connect(host='localhost', user='root', passwd='pankaj',database='stucouncil')
mycursor=mydb.cursor()
sql='show tables'
mycursor.execute(sql)               #executing SQL
myresult = mycursor.fetchall()          #fetching data from db
for data in myresult:
    print(data)
mydb.close()                                                    
