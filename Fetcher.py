import time
import mysql.connector


def Fetcher():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="DrugManagement"
    )
    mycursor = db.cursor()
    choice = int(input("Enter what do you want to search for:\n1. Name of drug (1)\n2. Manufacturer name (2)\n3. ID of drug (3)\n4. Quantity of drug (4)\n5. Manufacture Date (5)\n6. Expiry Date (6)\nYour Choice: "))
    print("=======================================================================================================")
    if choice == 1:
        name = input("Enter Name of Drug you want to search for: ")
        mycursor.execute(f"select * from drugdata where Name='{name}'")
        print("=======================================================================================================")
        print("Result:\n")
        print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
        for x in mycursor:
            print(x)
        print("=======================================================================================================")
        input("If nothing is shown under headers, the table is empty.\nPress ENTER to Exit!")
    elif choice == 2:
        Mname = input("Enter Name of Manufacturer: ")
        mycursor.execute(f"select * from drugdata where Manufacturer='{Mname}'")
        print("=======================================================================================================")
        print("Result:\n")
        print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
        for x in mycursor:
            print(x)
        print("=======================================================================================================")
        input("If nothing is shown under headers, the table is empty.\nPress ENTER to Exit!")
    elif choice == 3:
        ID = input("Enter ID of Drug you want to search for: ")
        mycursor.execute(f"select * from drugdata where ID='{ID}'")
        print("=======================================================================================================")
        print("Result:\n")
        print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
        for x in mycursor:
            print(x)
        print("=======================================================================================================")
        input("If nothing is shown under headers, the table is empty.\nPress ENTER to Exit!")
    elif choice == 4:
        qty = input("Enter Quantity of the drug: ")
        mycursor.execute(f"select * from drugdata where Quantity='{qty}'")
        print("=======================================================================================================")
        print("Result:\n")
        print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
        for x in mycursor:
            print(x)
        print("=======================================================================================================")
        input("If nothing is shown under headers, the table is empty.\nPress ENTER to Exit!")
    elif choice == 5:
        mfd = input("Enter Manufacture Date of the drug: ")
        mycursor.execute(f"select * from drugdata where Manufacture_Date='{mfd}'")
        print("=======================================================================================================")
        print("Result:\n")
        print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
        for x in mycursor:
            print(x)
        print("=======================================================================================================")
        input("If nothing is shown under headers, the table is empty.\nPress ENTER to Exit!")
    elif choice == 6:
        exp = input("Enter Expiry Date of the drug: ")
        mycursor.execute(f"select * from drugdata where Expiry_Date='{exp}'")
        print("=======================================================================================================")
        print("Result:\n")
        print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
        for x in mycursor:
            print(x)
        print("=======================================================================================================")
        input("If nothing is shown under headers, the table is empty.\nPress ENTER to Exit!")
    else:
        print("Wrong Input\nExitting in 5 seconds.")
        time.sleep(5)