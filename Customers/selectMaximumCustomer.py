import mysql.connector

# connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Iwaro123!",
    database="CustomerDB"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# correct SQL syntax and parameter style
sql = "SELECT * FROM Customers WHERE CustomerId = (SELECT MAX(CustomerId) FROM Customers);"
  # must be a tuple

cursorObject.execute(sql)
# printing all the recoords
for i in cursorObject:
    print(i)

#  commit the change to actually save it
dataBase.commit()
#print(sql)
print("maximum Id retrieved from Customers successfully")

# close the connection
dataBase.close()