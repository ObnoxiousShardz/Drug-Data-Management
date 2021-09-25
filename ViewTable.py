import mysql.connector


def Table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="DrugManagement"
    )
    mycursor = db.cursor()
    mycursor.execute("select * from drugdata")
    print("Name, Manufacturer, Quantity, Manufacture Date, Expiry Date, Unique ID")
    for x in mycursor:
        print(x)