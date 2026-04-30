import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Iwaro123!",
    database="personneldb"
)
try:
    
  cursorObject = dataBase.cursor()

  # Correct SQL syntax
  records = "INSERT INTO Employees (EmployeeId, Fullname, Email,ServiceId) VALUES (%s, %s, %s, %s)"

  # Use a list of tuples for multiple rows
  values = [
    (1, 'John Doe', 'johndoe@yahoo.com',1),
    (2, 'Bon Freight', 'bonfreight@yahoo.com',3),
    (3, 'George Shepard', 'georgeshepard@yahoo.com',2),
    (5, 'Lee Jung', 'leejung@yahoo.com',1)
  ]

  # Execute many records at once
  cursorObject.executemany(records, values)
  # Commit changes
  dataBase.commit()

  print(f"{cursorObject.rowcount} records inserted into Customers table successfully.")
except Exception as e:
  #SQLC.connection.rollback()
  print(f"Error!! either table does not exists or paramter not enough", "error")
finally:
 # finally closing the database connection
  dataBase.close()