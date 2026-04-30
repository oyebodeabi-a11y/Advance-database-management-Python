import mysql.connector

# Connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Iwaro123!",
    database="personneldb"
)

def selectrecords():
    cursorObject = dataBase.cursor()
    sql = "SELECT * FROM Employees"
    cursorObject.execute(sql)
    
    # print all the records
    for record in cursorObject.fetchall():
        print(record)


def updatetables():
    oldrowname = input("Enter old Fullname: ")
    newrowname = input("Enter new Fullname: ")
    
    cursorObject = dataBase.cursor()
    
    # Use placeholders (%s) for values
    sql = "UPDATE Employees SET Fullname = %s WHERE Fullname = %s"
    values = (newrowname, oldrowname)
    
    cursorObject.execute(sql, values)
    dataBase.commit()
    
    print("✅ Data updated in tbl_service successfully.")


# Run the functions
updatetables()
selectrecords()

# Close connection
dataBase.close()