'''
11-10-2020 Database Connectivity Program with Excel support
Database Name: xii_cs
Table Name: stud
CREATE TABLE stud (admno int(11) primary key AUTO_INCREMENT,
name varchar(30) DEFAULT NULL,
sex char(1) DEFAULT 'M',
cls int(11) DEFAULT NULL,
section char(1) DEFAULT NULL,
)

'''
import mysql.connector as conn
import datetime as d
import xlwt as xl

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

def getDate_Time():
    s=''
    dy=str(d.datetime.now().day)
    mo=str(d.datetime.now().month)
    yr=str(d.datetime.now().year)
    hr=str(d.datetime.now().hour)
    mi=str(d.datetime.now().minute)
    se=str(d.datetime.now().second)
    s=dy+mo+yr+hr+mi+se
    return s
    
def genExcel():
    wb = xl.Workbook()                                  # Workbook is created  
    sheet1 = wb.add_sheet('All_student')    # add_sheet is used to create sheet. 

    db=conn.connect(host='localhost', user='root', password='pankaj', database='xii_cs')
    myc=db.cursor()
    sql="desc stud"
    myc.execute(sql) 
    myresult=myc.fetchall()        

    Field_list=list()
    for data in myresult:
        Field_list.append(data[0])

    #print(Field_list)

    #Writing heading of table in Excel
    style=xl.easyxf('alignment: horizontal center')
    k=0
    for heading in Field_list:
        #print(k,heading)
        sheet1.write(0,k,heading,style=style)
        k=k+1

    #Now sending data to Excel
    sql='select * from stud order by admno'
    myc.execute(sql) 
    myresult=myc.fetchall()        

    row=1
    for data in myresult:
        column=0
        for i in range(len(Field_list)):
            if i!=1:
                sheet1.write(row,i,data[i],style=style)
            else:
                sheet1.write(row,i,data[i])
        row=row+1

    fnm='Student_'+getDate_Time()+str('.xls')
    wb.save(fnm) 
    print('Excel file \"',fnm,'\"created... Pls see your folder')
    
def main():
    a=True
    while a:
        print('1. Add record ')
        print('2. Show record')
        print('3. Generate Excel for student record')
        print('4. Update record')
        print('5. Delete record')
        print('6. Exit')
        ch=int(input('Enter your choice :'))

        if ch==1:
            insertRecord()
        elif ch==2:
            showRecord()
        elif ch==3:
            genExcel()
        elif ch==4:
            updateRecord()
        elif ch==5:
            deleteRecord()
        elif ch==6:
            a=False
        else:
            print('Enter proper choice')

#Execution of main program     
if __name__=='__main__':
    main()







