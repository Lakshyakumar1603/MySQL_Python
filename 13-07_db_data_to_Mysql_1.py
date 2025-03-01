#13-7-2020
#To send data from python to MySQL (db name :xii_cs, table : item)

import mysql.connector as con

try:
    mydb=con.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=mydb.cursor()

    name=input('Enter item name :')
    name=name.upper()

    check=True
    while check:
        rate=int(input('Enter rate :'))
        if rate>=0 and rate<=10000:
            check=False
    

    check=True
    while check:
        qty=int(input('Enter quantity :'))
        if qty>=0:
            check=False
    
    sql="insert into item(name, rate, qty) values('{}',{},{})".format(name,rate,qty)
    #print(sql)
    myc.execute(sql)
    mydb.commit()
    print('Data saved in the table')

except mysql.connector.Error as error:
    print('Sorry... some database error')
    print(error)



