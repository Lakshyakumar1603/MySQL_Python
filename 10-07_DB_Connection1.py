import mysql.connector as con

mydb=con.connect(host='localhost', user='root', password='pankaj',database='xibtp')
mycursor=mydb.cursor()
sql="select admno, name, sex from student where class=12 and sec='D'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for r in myresult:
	print(r)
 
