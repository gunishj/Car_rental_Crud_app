import sqlite3,os
import datetime

# import only system from os 
from os import system, name 
  
# define our clear function 
def clear(): 
      # for windows 
    if name == 'nt': 
        _ = system('cls') 
      # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
def Option_set():
        print("Would you like to choose the service from the given list of option below :")
        print("1. GetAllCars list of the cars present")
        print("2. SignUp New user")
        print("3. Login user")
        print("4. GetCarDetail")
        print("5. PostNewCar (for owners)")
        print("6. Book your Car ")
        print("7. exit")

def Create_DDL():
    db=sqlite3.connect('test.db')
    try:        
        cur =db.cursor()
        
        cur.execute('''CREATE TABLE User (        UserID INTEGER PRIMARY KEY AUTOINCREMENT,        name TEXT(20) NOT NULL,        address TEXT(50),        phnnum INTEGER,        email TEXT(50) NULL,        password TEXT(20) NOT NULL);''')

        cur.execute('''CREATE TABLE Cars (        CarID INTEGER PRIMARY KEY AUTOINCREMENT,        name TEXT(20) NOT NULL,        years INTEGER,        rent INTEGER, location TEXT(20));''')

        cur.execute('''CREATE TABLE Booking (        BookingID INTEGER PRIMARY KEY AUTOINCREMENT,        starttime date,        endtime date,        rent REAL ,         CarID INTEGER,        UserID INTEGER,        FOREIGN KEY (CarID)        REFERENCES Cars (CarID)         ON DELETE CASCADE,        FOREIGN KEY (UserID)        REFERENCES User (UserID)         ON DELETE CASCADE);''')
 
        print ('table created successfully')
    except:
        print ('error in operation')
        db.rollback()
    db.close()

def InsertIntoCar():
    db=sqlite3.connect('test.db')
    qry="insert into Cars (name, years, rent,location) values(?,?,?,?);"
    students=[('safari', 2018, 70,'delhi'), ('maruti 800', 2012, 13,'pune'),('buggati veyron', 2011, 70000,'delhi'),('polo', 2015, 100,'chennai'),('safari', 2018, 70,'mumbai'),('ambassdor', 1995, 70,'lucknow'),('i 10', 2012, 65,'pune'),('hummer', 2016, 110,'delhi')]
    try:
        cur=db.cursor()
        cur.executemany(qry, students)
        db.commit()
        print ("records added successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()

def InsertIntoUser():
    db=sqlite3.connect('test.db')
    qry="insert into User (name , address , phnnum ,email , password) values(?,?,?,?,?);"
    students=[('Amar', "a-1, loni, delhi -110021", 7200055512,"amar@gmail.com","qwert1234"), ('Deepak', "f-1, loni, delhi -110021", 92111479111,"Deepak@gmail.com","qwert1234")]
    try:
        cur=db.cursor()
        cur.executemany(qry, students)
        db.commit()
        print ("records added successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()

def SignupUser(name , address , phnnum ,email , password):
    db=sqlite3.connect('test.db')
    qry="insert into User (name , address , phnnum ,email , password) values(?,?,?,?,?);"
    students=[(name, address, phnnum,email,password)]
    try:
        cur=db.cursor()
        cur.executemany(qry, students)
        db.commit()
        print ("records added successfully")
    except:
        print ("error in operation")
        db.rollback()

    sql="SELECT * from user where name = (?)  ;"
    cur=db.cursor()
    students = [(name)]
    cur.execute(sql,students)
    students=cur.fetchall()
    print("The userid registered for username : ",name, " is ")
    for rec in students:
        print(rec)

    db.close()


def select():
    db=sqlite3.connect('test.db')
    sql="SELECT * from cars;"
    cur=db.cursor()
    cur.execute(sql)
    students=cur.fetchall()
    for rec in students:
        print(rec)
    db.close()

def GetAllCars(location):
    db=sqlite3.connect('test.db')
    location1=[(location)]
    sql="SELECT * from cars where location = (?) ;"
    cur=db.cursor()
    cur.execute(sql,location1)
    students=cur.fetchall()
    for rec in students:
        print(rec)
    db.close()

def LoginUser(usrName, password1):
    # need to check  for the password as well. 
    db=sqlite3.connect('test.db')
    login1=[(usrName)]
    sql="SELECT * from user where (name) = (?) ;"
    cur=db.cursor()
    cur.execute(sql,login1)
    students=cur.fetchall()
    for rec in students:
        print(rec)
    db.close()

def GetCarDetail(carid):
    db=sqlite3.connect('test.db')
    location1=[(carid)]
    sql="SELECT * from cars where carid = (?) ;"
    cur=db.cursor()
    cur.execute(sql,location1)
    students=cur.fetchall()
    for rec in students:
        print(rec)
    db.close()

def PostNewCar(name, years,rent,location):
    db=sqlite3.connect('test.db')
    qry="insert into Cars (name, years, rent,location) values(?,?,?,?);"
    students=[(name, years,rent,location)]
    try:
        cur=db.cursor()
        cur.executemany(qry, students)
        db.commit()
        print ("records added successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()  

def TotalRent(carid,userid,startdate,enddate):

    db=sqlite3.connect('test.db')
    carkey=[(carid)]
    sql="SELECT rent from cars where carid = (?) ;"
    cur=db.cursor()
    cur.execute(sql,carkey)
    carRent=cur.fetchall()
    for rec in carRent:
        print(rec)

    startdate=datetime.datetime.strptime(startdate,'%Y%m%d').date()
    enddate=datetime.datetime.strptime(enddate,'%Y%m%d').date()
    rent = carRent[0][0] * (enddate-startdate).days
    
    
    qry="insert into booking (starttime , endtime , rent ,  CarID , UserID) values(?,?,?,?,?);"    
    students=[(startdate,enddate,rent,carid,userid)]
 
    try:
        cur=db.cursor()
        cur.executemany(qry, students)
        db.commit()
        print ("Booking completed successfully and your total rent is: ")
    except:
        print ("error in operation")
        db.rollback()
        
    sql="SELECT rent from booking where userid = (?) ;"
    cur=db.cursor()
    students = [(userid)]
    cur.execute(sql,students)
    students=cur.fetchall()
    for rec in students:
        print(rec)

    db.close()