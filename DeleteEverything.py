import time

import mysql.connector

def DeleteEverything():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="DrugManagement"
    )
    choice = input("NOTHING CAN BE RECOVERED AFTER THE EXECUTION OF THIS PROGRAM!\nARE YOU SURE YOU WANT TO DELETE EVERYTHING FROM THE TABLE?\nYes/No: ")
    if choice.lower() == "yes":
        mycursor = db.cursor()
        mycursor.execute(f"delete from drugdata")
        mycursor.execute("ALTER TABLE drugdata AUTO_INCREMENT = 1")
        db.commit()
        print("=======================================================================================================")
        print("Everything was cleared\nThe table is empty now!\nQuitting program in 5 seconds.")
        time.sleep(5)
    else:
        print("=======================================================================================================")
        print("Ok!\nExecution Cancelled\nQuitting program in 5 seconds.")
        time.sleep(5)
