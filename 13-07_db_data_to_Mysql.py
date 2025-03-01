#13-7-2020
#To send data from python to MySQL (db name :xii_cs, table : item)

import mysql.connector as con

try:
    mydb=con.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=mydb.cursor()

    name=input('Enter item name :')
    name=name.upper()
    rate=int(input('Enter rate :'))
    qty=int(input('Enter quantity :'))
    
    sql="insert into item(name, rate, qty) values('"+name+"',"+str(rate)+","+str(qty)+")"
    #print(sql)
    myc.execute(sql)
    mydb.commit()
    print('Data saved in the table')

except mysql.connector.Error as error:
    print('Sorry... some database error')
    print(error)
