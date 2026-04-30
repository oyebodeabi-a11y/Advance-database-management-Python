import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Iwaro123!",
  database = "personneldb"
)
def showtables():
  
  Cursor = DataBase.cursor()
  Cursor.execute("SHOW TABLES")
  for i in Cursor:
    if len(i)>0:
      
      print(i)
    else:
      print("no tables to display")   
# Create a cursor object
Cursor = DataBase.cursor()
print("please enter the table to drop")
droptable=input()
# Execute command to create the database
Cursor.execute("DROP TABLE IF EXISTS " + droptable)

print("table dropped successfully")
# printing all the tables
showtables()

# finally closing the database connection
DataBase.close()