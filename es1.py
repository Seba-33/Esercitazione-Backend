#Creo database con python mysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"

)

mycursor = mydb.cursor()


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

