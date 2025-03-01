#06-10-2020 Database Connectivity

import mysql.connector as conn

def insertRecord():
    db=conn.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=db.cursor()
    admno=int(input('Enter admission number :'))
    name=input('Enter your name :')
    sex=input('Enter your gender (M/F/T) :')
    cls=int(input('Enter your class in number :'))
    section=input('Enter your section (A/B/C/D) :')

    name=name.upper()
    sex=sex.upper()
    section=section.upper()
    
    sql="insert into stud values({},'{}','{}',{},'{}')".format(admno,name,sex,cls,section)
    myc.execute(sql)
    db.commit()
    print('Record inserted . . .')

    myc.close()
    db.close()

def showRecord():
    db=conn.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=db.cursor()
    sql="select * from stud" 
    myc.execute(sql)
    res=myc.fetchall()
    k=myc.rowcount

    print('No of records are :',k)
    N=45
    print('Adm\tName\t\tSex\tClass\tSection')
    print('='*N)
    for record in res:
            print(record[0],"\t",record[1],"\t",record[2],"\t",record[3],"\t",record[4])
    print('='*N)    

    myc.close()
    db.close()

def updateRecord():
    db=conn.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=db.cursor()
    adm=int(input('Enter admission number to update record :'))
    print('Which detail you want to update?')
    print('Enter 1. Gender\t 2. Class\t 3. Section')
    k=int(input('Enter your choice (1/2/3) :'))
    if k==1:
        newsex=input('Enter sex :')
        sql="update stud set sex='{}' where admno={}".format(newsex,adm) 
    elif k==2:
        newcls=int(input('Enter class :'))
        sql="update stud set cls={} where admno={}".format(newcls,adm) 
    elif k==3:
        newsection=input('Enter section :')
        sql="update stud set section='{}' where admno={}".format(newsection,adm) 
    
    myc.execute(sql)
    db.commit()
    print('Record updated successfully . . .')    

    myc.close()
    db.close()
    
def deleteRecord():
    db=conn.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=db.cursor()
    adm=int(input('Enter admission number to delete record :'))
    sql="select * from stud where admno={}".format(adm)
    myc.execute(sql)
    res=myc.fetchall()
    norec=myc.rowcount

    if norec==1:
        sql="delete from stud where admno={}".format(adm) 
        myc.execute(sql)
        db.commit()
        print('Record deleted successfully . . .')    
    else:
        print('Sorry record does not exist')
              
    myc.close()
    db.close()
    
def main():
    a=True
    while a:
        print('1. Add record ')
        print('2. Show record')
        print('3. Update record')
        print('4. Delete record')
        print('5. Exit')
        ch=int(input('Enter your choice :'))

        if ch==1:
            insertRecord()
        elif ch==2:
            showRecord()
        elif ch==3:
            updateRecord()
        elif ch==4:
            deleteRecord()
        elif ch==5:
            a=False
        else:
            print('Enter proper choice')

#Execution of main program     
if __name__=='__main__':
    main()







