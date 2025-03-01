import mysql.connector as con
mydb=con.connect(host='localhost', user='root', password='pankaj')
mycursor=mydb.cursor()
sql='show databases;'
mycursor.execute(sql)
myresult=mycursor.fetchall()
for r in myresult:
	print(r)
