import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Iwaro123!"
)

# Create a cursor object
Cursor = DataBase.cursor()
print("please enter the database name to create")
createDB=input()
# Execute command to create the database
Cursor.execute("CREATE DATABASE " + createDB)

print("Database " + createDB + " is created")
Cursor.execute("SHOW DATABASES")

# printing all the databases
for i in Cursor:
    print(i)

Cursor = DataBase.cursor()

# finally closing the database connection
DataBase.close()
