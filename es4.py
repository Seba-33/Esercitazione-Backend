import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)