import sqlite3
import os
import threading
# import sleep to show output for some time period 
from time import sleep 
from first_module import *

if __name__ == '__main__':
            
    ## DB SETUP ##
    if os.path.exists("test.db"):
        os.remove("test.db")
    else:
        print("The file does not exist")

    open("test.db", 'a').close()

    t1 = threading.Thread(target=InsertIntoCar,name='t1')
    t2 = threading.Thread(target=InsertIntoUser,name='t2')
    
    Create_DDL()
    
    #starting threads 
    t1.start()
    t2.start()

    # InsertIntoCar()
    # InsertIntoUser()

    # waiting untill all threads are finished
    t1.join()
    t2.join()

    print("Welcome To gunish's Garage")
    print()
    
    while(True):
        # print out some text 
        print('Loading your web application\n'*3)         
        # sleep for 2 seconds after printing output 
        sleep(1)         
        # now call function we defined above 
        clear() 
        Option_set()

        inp_parm=input()
        inp_parm=int(inp_parm)
        if(int(inp_parm)==1):
            print("you chose: ", inp_parm)
            clear()
            print("Cars list")
            print("Please enter your location state:(ex: delhi) ")
            location=input()
            GetAllCars(location)
            print("press enter to go back to main menu")
            input()
            
        if(inp_parm==2):
            print("you chose: ", inp_parm)
            # sleep(1)
            clear()
            print("Sign UP")
            print("Please enter your name:(ex: gunish) ")
            name=input()
            print("Please enter your address:(ex: D-131,anand vihar , delhi-110092) ")
            address=input()
            print("Please enter your phnNum:(ex: 9871058942) ")
            phnNum=int(input())
            print("Please enter your email:(ex: gunish.jha.master@Gmail.com) ")
            email=input()
            print("Please enter your password:(ex: 12345678) ")
            password=input()
            SignupUser(name, address, phnNum, email, password)
            print("press enter to go back to main menu")
            input()

        if(inp_parm==3):
            print("you chose: ", inp_parm)
            # sleep(1)
            clear()
            print("Login User")
            print("Please enter your name:(ex: gunish) ")
            usrName=input()
            print("Please enter your password:(ex: 12345678) ")
            password=input()
            LoginUser(usrName, password)
            print("press enter to go back to main menu")
            input()

        if(inp_parm==4):
            print("you chose: ", inp_parm)
            # sleep(1)
            clear()
            print("Login User")
            print("Please enter your carId:(ex: 1) ")
            carId=int(input())
            GetCarDetail(carId)
            print("press enter to go back to main menu")
            input()

        if(inp_parm==5):
            print("you chose: ", inp_parm)
            # sleep(1)
            clear()
            print("Post your new Car")
            print("Please enter your carModelName:(ex: CRV) ")
            name = input()
            print("Please enter your carModelyear:(ex: 2019) ")
            years = int(input())
            print("Please enter your carsDailyRent:(ex: 100) ")
            rent = int(input())
            print("Please enter your carsCurrentLocation:(ex: Delhi) ")
            location = input()
            PostNewCar(name, years,rent,location)
            print("press enter to go back to main menu")
            input()

        if(inp_parm==6):
            print("you chose: ", inp_parm)
            # sleep(1)
            clear()
            print("Book the Car of your choice")
            print("Please enter your carsID you want to book:(ex: 1) ")
            carid=int(input())
            print("Please enter your UserID who wants to book:(ex: 1) ")
            userid=int(input())
            print("Please enter the date from which you want to start the booking in YYYYMMDD:(ex: 20201125) ")
            startdate=input()
            print("Please enter the date at which you want to end the booking in YYYYMMDD:(ex: 20201125) ")
            enddate=input()
            TotalRent(carid,userid,startdate,enddate)
            print("press enter to go back to main menu")
            input()

        if(inp_parm==7):
            break


    