# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Iwaro123!",
  database = "CustomerDB"
)
def showtables():
  
  cursorObject = dataBase.cursor()
  cursorObject.execute("SHOW TABLES")
  for i in cursorObject:
    if len(i)>0:
      
      print(i)
    else:
      print("no tables to display")  
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table a

Records = """CREATE TABLE IF NOT EXISTS Customers(...)
(CustomerId INT NOT NULL AUTO_INCREMENT,
             Customername VARCHAR(500) NOT NULL,
             Email VARCHAR(500) NOT NULL,
             ProductId INT,
             Date DATE,
              PRIMARY KEY (CustomerId)
                 )"""



# table created
cursorObject.execute(Records) 
print("Customers table created successfully")
showtables()
# disconnecting from server
dataBase.close()