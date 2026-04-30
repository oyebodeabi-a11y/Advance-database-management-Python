
import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Iwaro123!"
)

# Create a cursor object
Cursor = DataBase.cursor()

Cursor.execute("SHOW DATABASES")

# printing all the databases
for i in Cursor:
    print(i)

Cursor = DataBase.cursor()

# finally closing the database connection
DataBase.close()