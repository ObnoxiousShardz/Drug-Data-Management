import time

import mysql.connector


def Writer():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="DrugManagement"
    )
    mycursor = db.cursor()
    # mycursor.execute("create table DrugData (Name varchar(50),Manufacturer varchar (50),Quantity int, Manufacture_Date varchar (20), Expiry_Date varchar(20), ID int primary key auto_increment)")
    D_name = input("Enter name of the Drug: ")
    D_qty = int(input("Enter quantity of the drug units: "))
    D_man = input("Enter manufacturer name: ")
    D_mfd = input("Enter Manufacture Date (MFD) (example: 5th October 2019): ")
    D_exp = input("Enter Expiry Date (example: 31st December 2022): ")
    mycursor.execute(
        f"insert into drugdata (Name, Manufacturer,Quantity,Manufacture_Date,Expiry_Date) values (%s,%s,%s,%s,%s)",
        (f"{D_name}", f"{D_man}", f"{D_qty}", f"{D_mfd}", f"{D_exp}"))
    db.commit()
    print("=======================================================================================================")
    input("Entry was recorded successfully!\nPress ENTER to exit!")

