# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Iwaro123!",
  database = "personneldb"
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

Records = """CREATE TABLE Employees(
             EmployeeId INT NOT NULL AUTO_INCREMENT,
             Fullname VARCHAR(500) NOT NULL,
             Email VARCHAR(500) NOT NULL,
             ServiceId INT,
             PRIMARY KEY (EmployeeId)
                   )"""


# table created
cursorObject.execute(Records) 
print("Employees table created successfully")
showtables()
# disconnecting from server
dataBase.close()