import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Iwaro123!",
  database = "CustomerDB"
)
def showtables():
  
  Cursor = DataBase.cursor()
  Cursor.execute("SHOW TABLES")
  for i in Cursor:
    if len(i)>0:
      
      print(i)
    else:
      print("no tables to display")   

# printing all the tables
showtables()