import time

import mysql.connector

def Clearer():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="DrugManagement"
    )
    mycursor = db.cursor()
    choice = int(input("Enter the ID of the drug, which you want to delete: "))
    mycursor.execute(f"delete from drugdata where ID={choice}")
    db.commit()
    print("=======================================================================================================")
    print("Entry deleted successfully!\nExitting in 5 seconds")
    time.sleep(5)